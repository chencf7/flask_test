# coding=utf-8
import os
from flask_script import Manager, Command

from flask_test import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


# flask_script自定义命令两种方式
# 使用add_command自定义 python run.py hello1
class Hello(Command):
    def run(self):
        print('hello world')


manager.add_command('hello1', Hello())

# 使用装饰器@manager.command自定义 python run.py hello2
@manager.command
def hello2():
    print("server is running")


if __name__ == '__main__':
    manager.run()
