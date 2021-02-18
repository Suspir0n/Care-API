from flask import Flask
from .settings.connection import connect_db
from flask_jwt_extended import JWTManager
from flask_restful import Api
from .blacklist import BLACKLIST
from .settings.config import config_db, config_ma, config_bp, secret_key, config_JWT

def create_app():
    app = Flask(__name__)
    connect_db(app)
    config_db(app)
    config_ma(app)
    config_bp(app)
    config_JWT(app)
    secret_key(app)
    return app

app = create_app()
api = Api(app)
jwt = JWTManager(app)
# decorador para verificar se o token esta autenticado
@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, jwt_data):
    # verifica se o id do token esta dentro da blacklist retornando True ou False
    return jwt_data['jti'] in BLACKLIST


# Se caso o token não esteja autenticado executa a função do decorador
@jwt.revoked_token_loader
def token_invalid():
    return jsonify({'message': "this token has already been logged out"}), 401
