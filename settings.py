# -*- coding: utf-8 -*-
# @Author: Zengjq
# @Date:   2018-06-07 23:52:51
# @Last Modified by:   Zengjq
# @Last Modified time: 2019-03-18 16:51:12
import os
import configparser
script_path = os.path.split(os.path.realpath(__file__))[0].replace('\\', '/')

conf = configparser.ConfigParser()
conf.read(os.path.join(script_path, 'ankiweb.conf'))
config = conf['web_app']
debug = conf.getboolean('web_app', 'debug')
listen_IP = conf.get('web_app', 'listen_IP')
listen_port = conf.get('web_app', 'listen_port')
context_path = conf.get('web_app', 'context_path')
secret_key = conf.get('web_app', 'secret_key')
anki_sync_server_path = conf.get('web_app', 'anki_sync_server_path')
data_root = os.path.join(anki_sync_server_path,'collections')
base_url = conf.get('web_app', 'base_url')
base_media_url = conf.get('web_app', 'base_media_url')
auth_db_path = os.path.join(anki_sync_server_path,'auth.db')
session_db_path = os.path.join(anki_sync_server_path,'session.db')
force_https = conf.getboolean('web_app', 'force_https')