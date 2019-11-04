# coding=utf-8

import os


class BaseConfig(object):
    # 防止CSRF攻击的用于生成token的字符串
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SALT = os.environ.get('SALT')


# 继承base的基础配置， 开发环境配置
class DevConfig(BaseConfig):
    DEBUG = True


# 生产环境配置
class ProdConfig(BaseConfig):
    DEBUG = False


config = {
    'development': DevConfig,
    'production': ProdConfig,

    'default': DevConfig
}
