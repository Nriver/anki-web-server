from flask import Blueprint
from flask import jsonify

api_status = Blueprint('api_status', __name__)


@api_status.route('/')
def echo():
    return jsonify({'code': 20000, "status": "ok"})
