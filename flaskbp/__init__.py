from flask import Flask

from flaskbp.api.login import api_login
from flaskbp.api.card import api_card
from flaskbp.api.deck import api_deck
from flaskbp.api.status import api_status
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
        if context_path:
            return '/' + context_path + sub_url
        return sub_url

    app = Flask(__name__, static_url_path=add_url_prefix('/static'), static_folder='static')
    app.secret_key = 'secret_key'

    app.config['DEBUG'] = debug
    if debug:
        app.logger.setLevel(logging.DEBUG)

    app.register_blueprint(bp_index, url_prefix=add_url_prefix('/'))
    app.register_blueprint(bp_login, url_prefix=add_url_prefix('/login'))
    app.register_blueprint(bp_decks, url_prefix=add_url_prefix('/decks'))
    app.register_blueprint(bp_cards, url_prefix=add_url_prefix('/cards'))

    # api for vue
    app.register_blueprint(api_status, url_prefix=add_url_prefix('/api/status'))
    app.register_blueprint(api_login, url_prefix=add_url_prefix('/api/auth'))
    app.register_blueprint(api_deck, url_prefix=add_url_prefix('/api/deck'))
    app.register_blueprint(api_card, url_prefix=add_url_prefix('/api/card'))

    if force_https:
        app.config.update(dict(
            PREFERRED_URL_SCHEME='https'
        ))

    return app
