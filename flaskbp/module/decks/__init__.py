# -*- coding: utf-8 -*-
# @Author: Zengjq
# @Date:   2019-03-18 15:37:04
# @Last Modified by:   Zengjq
# @Last Modified time: 2019-03-19 20:31:08
from flask import Blueprint

bp_decks = Blueprint('decks', __name__)

from . import views
