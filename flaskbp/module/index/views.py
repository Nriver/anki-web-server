from flask import url_for, redirect

from flaskbp.module.index import bp_index


@bp_index.route('/')
def index():
    return redirect(url_for('login.login_page'))
