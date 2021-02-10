from flask import Flask
from .settings.connection import connect_db
from .settings.config import config_db, config_ma, config_bp, secret_key

def create_app():
    app = Flask(__name__)
    connect_db(app)
    config_db(app)
    config_ma(app)
    config_bp(app)
    secret_key(app)
    return app

