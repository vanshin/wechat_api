#coding=utf-8

from flask import Flask

def create_app(config_name):
    app = Flask(__name__)
    app.secret_key = 'vanshin'

    # 初始化组件

    # 蓝图

    from .menu import menu as menu_blueprint
    app.register_blueprint(menu_blueprint)

    return app
