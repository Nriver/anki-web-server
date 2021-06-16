from flask import Blueprint

bp_login = Blueprint('login', __name__)

from . import views
