from flask import Blueprint

bp_index = Blueprint('index', __name__)

from . import views
