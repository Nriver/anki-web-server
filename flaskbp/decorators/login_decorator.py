# -*- coding: utf-8 -*-
# @Author: Zengjq
# @Date:   2019-03-19 20:07:23
# @Last Modified by:   Zengjq
# @Last Modified time: 2019-03-19 20:21:02

from functools import wraps
from flask import request, redirect, url_for, session


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
            print('unauthorized access from %s to %s' % (ip, request.endpoint))
            return redirect(url_for('login.login_page'))
        return f(*args, **kwargs)
    return decorated_function
