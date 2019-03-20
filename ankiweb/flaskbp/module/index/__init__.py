# -*- coding: utf-8 -*-
# @Author: Zengjq
# @Date:   2018-06-04 12:15:18
# @Last Modified by:   Zengjq
# @Last Modified time: 2018-06-04 16:07:48
from flask import Blueprint

bp_index = Blueprint('index', __name__)

from . import views
