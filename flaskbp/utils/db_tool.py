import sqlite3
from settings import data_root, auth_db_path
from flask import g, session, render_template, request
from anki import Collection


def get_auth_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(auth_db_path)
    return db


def get_collection(username):
    col = getattr(g, '_collection', None)
    if col is None:
        collection_path = data_root + '/' + username + '/collection.anki2'
        # col = g._collection = Collection(collection_path, lock=True)
        col = g._collection = Collection(collection_path, server=True)
    return col
