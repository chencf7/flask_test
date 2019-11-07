# coding=utf-8
"""
使用 flask_script，flask_migrate同步数据库
数据库迁移操作指令
创建迁移仓库：python db_migrate.py db init，只需要初始化时执行依次即可

自动创建迁移脚本：python db_migrate.py db migrate [-m "initial migrate"]
更新数据库：python db_migrate.py db upgrade

注意：使用自定创建脚本命令，会在 /migrations/versions/ 文件夹下自动生成一个脚本，upgrade命令即执行该脚本
migrate同步数据库会删除数据库中本来存在，但未有映射的表，请谨慎操作
"""
import os
from flask_script import Manager, Command
from flask_migrate import Migrate, MigrateCommand

from flask_test import create_app
from flask_test.common.dbexts import db

# 此处必须添加model引入，否则不会迁移
from flask_test.models.User import User

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app=app, db=db)

'''向flask_script命令行解释器添加db相关操作的命令'''
manager.add_command('db', MigrateCommand)

# flask_script自定义命令两种方式
# 使用add_command自定义 python run.py hello1
# 使用装饰器@manager.command自定义 python run.py hello2

if __name__ == '__main__':
    manager.run()
