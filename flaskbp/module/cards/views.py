import html
import re

from flask import session, render_template, request, jsonify, url_for, send_from_directory, redirect

from flaskbp.decorators.login_decorator import login_required
from flaskbp.module.cards import bp_cards
from flaskbp.utils.db_tool import get_collection
from settings import data_root


def all_sounds(text):
    _soundReg = r"\[sound:(.*?)\]"
    match = re.findall(_soundReg, text)
    sound_list = list(map(html.unescape, match))
    return sound_list


@bp_cards.route('/study')
@login_required
def card_study():
    col = get_collection(session['current_user']['username'])
    col.reset()
    card = col.sched.getCard()
    if card is None:
        return redirect(url_for('decks.deck_overview'))
    question = card.q()
    answer = card.a()
    # 把声音文件名拿出来
    question_sound_list = all_sounds(question)
    answer_sound_list = all_sounds(answer)
    # 前端不显示声音信息
    question = re.sub(r"\[sound:[^]]+\]", "", question)
    answer = re.sub(r"\[sound:[^]]+\]", "", answer)
    print(question_sound_list)
    print(answer_sound_list)

    # 处理图片
    # url_for('cards.card_media',filename=img)
    reMedia = re.compile("(?i)(<img[^>]+src=[\"']?)([^\"'>]+[\"']?[^>]*>)")
    media_url_prefix = url_for('cards.card_media', filename="")
    question = reMedia.sub(" \\1" + media_url_prefix + "\\2", question)
    answer = reMedia.sub(" \\1" + media_url_prefix + "\\2", answer)

    cnt = col.sched.answerButtons(card)
    if cnt == 2:
        btn_list = [(1, 'Again'), (2, 'Good')]
    elif cnt == 3:
        btn_list = [(1, 'Again'), (2, 'Good'), (3, 'Easy')]
    else:
        btn_list = [(1, 'Again'), (2, 'Hard'), (3, 'Good'), (4, 'Easy')]

    col.close()
    html = render_template('cards/card_study.htm', **locals())
    return html


@bp_cards.route('/answer', methods=['POST'])
@login_required
def card_answer():
    answer = request.values.get('answer')
    col = get_collection(session['current_user']['username'])
    col.reset()
    card = col.sched.getCard()
    sched = col.sched
    sched.answerCard(card, int(answer))
    col.close()
    return jsonify({"result": True, "next": url_for('cards.card_study')})


@bp_cards.route('/media/<filename>')
@login_required
def card_media(filename):
    # 关键是参考 playFromText
    username = session['current_user']['username']
    media_path = data_root + '/' + username + '/collection.media'
    print('media_path', media_path)
    print('filename', filename)
    return send_from_directory(media_path, filename)
