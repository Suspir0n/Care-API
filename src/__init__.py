from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from .setting.connection import SQLALCHEMY_DATABESE_URI

app = Flask(__name__)


def config_database():
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABESE_URI


def init_db():
    db = SQLAlchemy(app)
    ma = Marshmallow(app)
    database = {'SQLAlchemy': db, 'Marshmallow': ma}
    return database