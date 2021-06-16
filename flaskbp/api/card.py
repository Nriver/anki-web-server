import html
import re

from flask import request, jsonify, url_for, send_from_directory, redirect, Blueprint

from flaskbp.decorators.login_decorator import jwt_required
from flaskbp.utils.db_tool import get_collection
from flaskbp.utils.jwt_tool import decrypt_token
from settings import data_root, media_domain

api_card = Blueprint('api_card', __name__)


@api_card.route('/study')
@jwt_required
def card_study():
    username = decrypt_token(request.headers['auth'])['username']
    col = get_collection(username)
    col.reset()
    card = col.sched.getCard()
    if card is None:
        return redirect(url_for('api_deck.deck_overview'))
    question = card.question()
    answer = card.answer()

    # 媒体文件域名在设置里配置
    # 媒体文件uri前缀
    media_url_prefix = url_for('api_card.card_media', username=username, filename="")
    # 把声音文件名拿出来
    # question_sound_list = all_sounds(question)
    # answer_sound_list = all_sounds(answer)
    # 接口变了
    question_sound_list = [media_domain + media_url_prefix + x.filename for x in card.question_av_tags()]
    answer_sound_list = [media_domain + media_url_prefix + x.filename for x in card.answer_av_tags()]
    print('question_sound_list', question_sound_list)
    print('answer_sound_list', answer_sound_list)
    # 前端不显示声音信息
    # question = re.sub(r"\[sound:[^]]+\]", "", question)
    # answer = re.sub(r"\[sound:[^]]+\]", "", answer)
    question = re.sub(r"\[anki:play[^]]+\]", "", question)
    answer = re.sub(r"\[anki:play[^]]+\]", "", answer)

    # 处理图片
    # url_for('api_card.card_media',filename=img)
    reMedia = re.compile("(?i)(<img[^>]+src=[\"']?)([^\"'>]+[\"']?[^>]*>)")
    question = reMedia.sub(" \\1" + media_domain + media_url_prefix + "\\2", question)
    answer = reMedia.sub(" \\1" + media_domain + media_url_prefix + "\\2", answer)
    # print('============ question ============')
    # print(question)
    # print('============ answer ============')
    # print(answer)
    # print('==================================')
    cnt = col.sched.answerButtons(card)
    if cnt == 2:
        btn_list = [(1, 'Again'), (2, 'Good')]
    elif cnt == 3:
        btn_list = [(1, 'Again'), (2, 'Good'), (3, 'Easy')]
    else:
        btn_list = [(1, 'Again'), (2, 'Hard'), (3, 'Good'), (4, 'Easy')]

    col.close()
    return jsonify({'code': 20000,
                    'question': question,
                    'answer': answer,
                    'question_sound_list': question_sound_list,
                    'answer_sound_list': answer_sound_list,
                    'btn_list': btn_list,
                    })


@api_card.route('/answer', methods=['POST'])
@jwt_required
def card_answer():
    answer = request.json['answer']
    col = get_collection(decrypt_token(request.headers['auth'])['username'])
    col.reset()
    card = col.sched.getCard()
    sched = col.sched
    sched.answerCard(card, int(answer))
    col.close()
    return jsonify({"code": 20000})


@api_card.route('/media/<username>/<filename>')
# @jwt_required
def card_media(username, filename):
    # 关键是参考 playFromText
    # username = decrypt_token(request.headers['auth'])['username']
    media_path = data_root + '/' + username + '/collection.media'
    print('media_path', media_path)
    print('filename', filename)
    return send_from_directory(media_path, filename)


def all_sounds(text):
    _soundReg = r"\[sound:(.*?)\]"
    match = re.findall(_soundReg, text)
    sound_list = list(map(html.unescape, match))
    return sound_list