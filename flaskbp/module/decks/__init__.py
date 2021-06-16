from flask import Blueprint

bp_decks = Blueprint('decks', __name__)

from . import views
