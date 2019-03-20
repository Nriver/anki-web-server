# -*- coding: utf-8 -*-
# @Author: Zengjq
# @Date:   2018-06-04 12:15:18
# @Last Modified by:   Zengjq
# @Last Modified time: 2019-03-19 20:43:07

from flaskbp.module.login import bp_login
from flask import render_template, request, redirect, jsonify, session, url_for
from flask import current_app as app
import hashlib
from flaskbp.decorators.login_decorator import login_required


@bp_login.route('/')
def login_page():
    html = render_template('login/login_page.htm', **locals())
    return html


@bp_login.route('/do_login', methods=['POST'])
def do_login():
    print('do_login()')
    username = request.values.get('username')
    password = request.values.get('password')
    print(username)
    print(password)
    session['logged_in'] = True
    session['current_user'] = {'username': username}
    return jsonify({"result": True, "next": url_for('decks.decks_list')})


@bp_login.route('/logout')
@login_required
def logout():
    print('user logout')
    session.pop('logged_in')
    session.pop('current_user')
    return redirect(url_for('login.login_page'))
