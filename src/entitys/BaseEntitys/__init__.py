from datetime import datetime
from src import init_db

database = init_db()


class BaseEntitys(database['SQLAlchemy'].Model):
    uid = database['SQLAlchemy'].Column(database['SQLAlchemy'].String(100), primary_Key=True)
    active = database['SQLAlchemy'].Column(database['SQLAlchemy'].Boolean, default=True)
    deleted = database['SQLAlchemy'].Column(database['SQLAlchemy'].Boolean, default=False)
    createAt = database['SQLAlchemy'].Column(database['SQLAlchemy'].Datetime, default=datetime.now())
    updateAt = database['SQLAlchemy'].Column(database['SQLAlchemy'].Datetime, default=datetime.now())