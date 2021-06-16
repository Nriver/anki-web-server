from flask import jsonify, request

from flaskbp.decorators.login_decorator import jwt_required
from flaskbp.utils.db_tool import get_collection
from flaskbp.utils.jwt_tool import decrypt_token
from flask import Blueprint

api_deck = Blueprint('api_deck', __name__)


@api_deck.route('/list')
@jwt_required
def decks_list():
    user_info = decrypt_token(request.headers.get('auth', None))
    username = user_info['username']
    col = get_collection(username)
    decks = col.decks
    deck_list = []
    dueTree = col.sched.deckDueTree()
    for node in dueTree:
        name, did, due, lrn, new, children = node
        if did == 1:
            continue
        deck_list.append({'name': name, 'did': did, 'new': new})

    card_count, learn_time = col.db.first("""
    select count(), sum(time)/1000 from revlog
    where id > ?""", (col.sched.dayCutoff - 86400) * 1000)
    col.close()
    return jsonify({'code': 20000, "deck_list": deck_list, "card_count": card_count, "learn_time": learn_time})


@api_deck.route('/overview', defaults={'did': None})
@api_deck.route('/overview/<did>')
@jwt_required
def deck_overview(did):
    username = decrypt_token(request.headers['auth'])['username']
    col = get_collection(username)
    decks = col.decks
    if did:
        # 切换deck
        col.decks.select(did)
    # 查看现在选中的deck (返回的是dict)
    # col.decks.current() 效果和 col.decks.decks[did] 是一样的
    deck = decks.current()
    # 计划
    sched = col.sched
    # 统计数字
    sched.reset()
    # deck首页的几个数字
    newCount, lrnCount, revCount = sched.counts()
    print(newCount, lrnCount, revCount)
    finished = not sum([newCount, lrnCount, revCount])
    col.close()
    return jsonify({'code': 20000,
                    "deck": deck,
                    "newCount": newCount,
                    "lrnCount": lrnCount,
                    "revCount": revCount,
                    "finished": finished,
                    })

