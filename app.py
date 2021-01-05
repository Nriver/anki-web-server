# -*- coding: utf-8 -*-
# @Author: Zengjq
# @Date:   2019-03-14 19:40:47
# @Last Modified by:   Zengjq
# @Last Modified time: 2019-03-20 18:36:21
import os
import sys
from pathlib import Path
from flask import g, session, request, redirect, url_for
import traceback
# script_path = os.path.split(os.path.realpath(__file__))[0].replace('\\', '/')
#sys.path.insert(0, os.path.join(Path(script_path).parent, "anki-bundled"))

from flaskbp import create_app

from settings import listen_IP, listen_port, context_path, secret_key, data_root, base_url, base_media_url, auth_db_path, session_db_path

app = create_app('')


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

    col = getattr(g, '_collection', None)
    if col is not None:
        col.close()


@app.errorhandler(Exception)
def all_exception_handler(e):
    # 报错先关db连接再说
    close_connection(e)
    print('ERROR!:', (e))
    print(request.args)
    print('============all_exception_handler================')
    # traceback.print_exc()
    traceback_message = traceback.format_exc()
    print('traceback_message\n', traceback_message)
    # write error log with traceback_message
    pass
    print('==========================================')
    return '---Exception---', 404

if __name__ == '__main__':
    app.run(host=listen_IP, port=int(listen_port))
