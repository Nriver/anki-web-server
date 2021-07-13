from flask import render_template, session

from flaskbp.decorators.login_decorator import login_required
from flaskbp.module.decks import bp_decks
from flaskbp.utils.db_tool import get_collection
from flaskbp.utils.jwt_tool import decrypt_token

@bp_decks.route('/list')
@login_required
def decks_list():
    col = get_collection(session['current_user']['username'])
    decks = col.decks
    deck_list = []
    dueTree = col.sched.deckDueTree()
    for node in dueTree:
        name, did, due, lrn, new, children = node
        if did == 1:
            continue
        sub_deck = []
        for sub_node in children:
            sub_name, sub_did, sub_due, sub_lrn, sub_new, sub_children = sub_node
            sub_deck.append({'name': sub_name, 'did': sub_did, 'new': sub_new})
        deck_list.append({'name': name, 'did': did, 'new': new, 'sub_deck': sub_deck})

    cards, thetime = col.db.first("""
    select count(), sum(time)/1000 from revlog
    where id > ?""", (col.sched.dayCutoff - 86400) * 1000)
    col.close()
    html = render_template('decks/decks_list.htm', **locals())
    return html


@bp_decks.route('/overview', defaults={'did': None})
@bp_decks.route('/overview/<did>')
@login_required
def deck_overview(did):
    col = get_collection(session['current_user']['username'])
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
    # print(newCount, lrnCount, revCount)
    finished = not sum([newCount, lrnCount, revCount])
    col.close()
    html = render_template('decks/deck_overview.htm', **locals())
    return html
