from functools import wraps
from flask import request, redirect, url_for, session
from flaskbp.utils.jwt_tool import decrypt_token

def login_required(f):
    # request decorator
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
            print('unauthorized access from %s to %s' % (ip, request.endpoint))
            return redirect(url_for('login.login_page'))
        return f(*args, **kwargs)
    return decorated_function


def jwt_required(f):
    # api decorator
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('auth', None)
        user_info = decrypt_token(token)
        if not user_info:
            ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
            print('unauthorized access from %s to %s' % (ip, request.endpoint))
            return {'code': 50008}
        return f(*args, **kwargs)
    return decorated_function
