from flask import Flask
from .settings.connection import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from .settings.config import config_db, config_ma

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
    config_db(app)
    config_ma(app)

    from .books import bp_books
    from .routes.user_routes import bp_users
    app.register_blueprint(bp_books)
    app.register_blueprint(bp_users)
    return app

