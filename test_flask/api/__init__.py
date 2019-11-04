# coding=utf-8

from flask import Blueprint

'''
蓝图
存储操作路由映射方法的容器
主要用来实现客户端请求和URL相互关联的功能
实现模块化应用的功能
'''
bp_api = Blueprint('flask_api', __name__)

from . import LoginCtrl, SystemCtrl