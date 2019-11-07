from datetime import datetime
from ..common.dbexts import db


class User(db.Model):
    # 用户类

    # 表名
    __tablename__ = 'flask_user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, index=True)
    email = db.Column(db.String(255), unique=True, index=True)
    last_login = db.Column(db.DateTime, default=datetime.utcnow)
