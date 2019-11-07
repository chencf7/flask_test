# coding=utf-8

import os

USERNAME = 'root'
PASSWORD = 'dhcc'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'repo_monitor'


class BaseConfig(object):
    # 防止CSRF攻击的用于生成token的字符串
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SALT = os.environ.get('SALT')


# 继承base的基础配置， 开发环境配置
class DevConfig(BaseConfig):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:dhcc@localhost:3306/irp_web'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@localhost:3306/{}'.format(USERNAME, PASSWORD, DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS = True


# 生产环境配置
class ProdConfig(BaseConfig):
    DEBUG = False


config = {
    'development': DevConfig,
    'production': ProdConfig,

    'default': DevConfig
}
