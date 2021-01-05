# -*- coding: utf-8 -*-
# @Author: Zengjq
# @Date:   2019-03-18 15:37:04
# @Last Modified by:   Zengjq
# @Last Modified time: 2019-03-20 18:43:52
import os
import sqlite3
import hashlib
from flask import g, session, render_template, request
from flaskbp.module.decks import bp_decks
from flaskbp.decorators.login_decorator import login_required
from flaskbp.utils.db_util import get_auth_db, get_collection
from settings import config, data_root, auth_db_path
from anki import Collection

import anki.db
import anki.sync
import anki.utils


@bp_decks.route('/list')
@login_required
def decks_list():

    col = get_collection()
    decks = col.decks
    deck_list = []
    dueTree = col.sched.deckDueTree()
    for node in dueTree:
        name, did, due, lrn, new, children = node
        if did == 1:
            continue
        deck_list.append({'name': name, 'did': did, 'new': new})

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
    col = get_collection()
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
    html = render_template('decks/deck_overview.htm', **locals())
    return html
