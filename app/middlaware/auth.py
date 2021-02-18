import datetime
from flask_jwt_extended import create_access_token, jwt_required
from flask_restful import Resource, reqparse
from flask import request, jsonify, current_app
from ..controllers.user_controller import user_by_auth
from werkzeug.security import safe_str_cmp, check_password_hash
from ..blacklist import BLACKLIST
from ..models.user_model import UserModel

arguments = reqparse.RequestParser()
arguments.add_argument('email', type=str, required=True, help="The filnds 'Email' cannot be left blank")
arguments.add_argument('password', type=str, required=True, help="The filnds 'password' cannot be left blank")

# Gerando token com base na Secret key do app e definindo expiração com 'exp'
def auth():
    auth = [request.json['email'], request.json['password']]
    check_credential_exits(auth[0], auth[1])
    user = user_by_auth(auth[0])
    if not user:
        return jsonify({'status': 400,'message': 'Este usuario não existe, por favor efetue o registro!'})

    if user and check_password_hash(user.password, auth[1]):
        # Cria um token de acesso para o id do usuario logado
        token_access = create_access_token(identity=user.uid)
        return jsonify({'message': 'Validated successfully', 'token': token_access,
                        'exp': datetime.datetime.now() + datetime.timedelta(hours=12)}), 200
    return jsonify({'message': 'The username or password is incorrect.'}), 401


def check_credential_exits(email, password):
    if not email or not password:
        return jsonify({'status': 400, 'message': 'Informe o email e a senha para efetuar o login!'})


"""# Classe para Logout do usuario
class UserLogout(Resource):
    # decorador - é preciso estar logado para fazer logout
    @jwt_required
    def post(self):
        # Pega o id do token do usuario logado
        jwt_id = get_raw_jwt()['jti']
        # adiciona dentro da blacklist
        BLACKLIST.add(jwt_id)
        return {'message': 'Successfully Logged Out'}
"""