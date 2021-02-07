from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def config_db(app):
    db.init_app(app)
    app.app_context().push()
    db.create_all(app=app)
    app.db = db


def config_ma(app):
    ma.init_app(app)