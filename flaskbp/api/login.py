from datetime import datetime, timedelta

from flask import Blueprint
from flask import request, jsonify, session

from flaskbp.decorators.login_decorator import jwt_required
from flaskbp.utils.jwt_tool import encrypt_token

api_login = Blueprint('api_login', __name__)


@api_login.route('/login', methods=['POST'])
def login():
    print('login()')
    username = request.json['username']
    password = request.json['password']
    print(username)
    print(password)

    # 密码没有验证?

    # use jwt for auth
    token_info = {
        'username': username,
        'expire': int((datetime.now() + timedelta(minutes=30)).timestamp()),
    }

    token_string = encrypt_token(token_info)

    return jsonify({'code': 20000, 'next': '/deck/list', 'token': token_string})


@api_login.route('/logout')
@jwt_required
def logout():
    print('user logout')
    session.pop('logged_in')
    session.pop('current_user')
    return jsonify({'code': 20000, "next": "/login"})
