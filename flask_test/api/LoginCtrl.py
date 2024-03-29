# coding=utf-8

from flask import current_app, request, make_response, jsonify, session
from flask_test.api import bp_api

# 测试方法
@bp_api.route('/test', methods=['GET'])
def test():
    return jsonify(type='ok', msg='test111 success')


# 登陆验证方法
@bp_api.route('/login', methods=['POST'])
def login():
    un = request.json.get('username')
    pwd = request.json.get('passwd')

    return jsonify(type='ok', msg='login success', un=un)
  

