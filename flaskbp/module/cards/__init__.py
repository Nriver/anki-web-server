from flask import Blueprint

bp_cards = Blueprint('cards', __name__)

from . import views
