# coding=utf-8

from flask import current_app, request, make_response, jsonify, session

from test_flask.api import bp_api

# 测试方法
@bp_api.route('/orginfo', methods=['GET'])
def orginfo():
  return jsonify(type='ok', msg='get orginfo')
  

