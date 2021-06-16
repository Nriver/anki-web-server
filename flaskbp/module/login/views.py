from flask import render_template, request, redirect, jsonify, session, url_for

from flaskbp.decorators.login_decorator import login_required
from flaskbp.module.login import bp_login


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
