# -*- coding: utf-8 -*-
# @Author: Zengjq
# @Date:   2018-06-04 12:15:18
# @Last Modified by:   Zengjq
# @Last Modified time: 2019-03-20 13:24:07

from flaskbp.module.index import bp_index
from flask import render_template, url_for, redirect


@bp_index.route('/')
def index():
    return redirect(url_for('login.login_page'))
