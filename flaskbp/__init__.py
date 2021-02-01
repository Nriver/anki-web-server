# -*- coding: utf-8 -*-
# @Author: Zengjq
# @Date:   2018-06-07 21:43:49
# @Last Modified by:   Zengjq
# @Last Modified time: 2019-03-20 18:38:00
from flask import Flask
from flaskbp.module.index import bp_index
from flaskbp.module.login import bp_login
from flaskbp.module.decks import bp_decks
from flaskbp.module.cards import bp_cards
import logging
from settings import debug, context_path, force_https


def create_app(configName):
    """
    app factory
    """

    def add_url_prefix(sub_url):
        return "/" + context_path + sub_url

    app = Flask(__name__, static_url_path='/' + context_path + '/static', static_folder='static')
    app.secret_key = 'secret_key'

    app.config['DEBUG'] = debug
    if debug:
        app.logger.setLevel(logging.DEBUG)

    app.register_blueprint(bp_index, url_prefix=add_url_prefix("/"))
    app.register_blueprint(bp_login, url_prefix=add_url_prefix("/login"))
    app.register_blueprint(bp_decks, url_prefix=add_url_prefix("/decks"))
    app.register_blueprint(bp_cards, url_prefix=add_url_prefix("/cards"))

    if force_https:
        app.config.update(dict(
            PREFERRED_URL_SCHEME = 'https'
        ))

    return app
