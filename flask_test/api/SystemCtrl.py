# coding=utf-8

# from flask import current_app, request, make_response, jsonify, session
from flask import jsonify

from flask_test.api import bp_api
from ..common.dbexts import db
from ..models.User import User

# 测试方法
@bp_api.route('/getinfo', methods=['GET'])
def getinfo():
    return jsonify(type='ok', msg='get info')

# 测试add方法
@bp_api.route('/adduser', methods=['GET'])
def add_user():
    new_user = User(id=1, username='chen')
    db.session.add(new_user)
    db.session.commit()
    return jsonify(type='ok', msg='data add success')
