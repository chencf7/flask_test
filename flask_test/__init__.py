# coding=utf-8

from flask import Flask, render_template
from config import config
from .common.dbexts import db


def create_app(app_env):
    app = Flask(__name__, template_folder="../templates")
    app.config.from_object(config[app_env])
    db.init_app(app=app)

    # 初始化index页面
    @app.route('/', methods=['GET'])
    def index():
        return render_template('index.html')

    # 注册api blueprint
    from flask_test.api import bp_api as api_v1
    app.register_blueprint(api_v1, url_prefix='/api')
    # from app.api_v1 import api as api_v1_0_blueprint
    # app.register_blueprint(api_v1_0_blueprint, url_prefix='/api/v1.0')

    return app
