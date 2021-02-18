import datetime
from functools import wraps
from flask import request, jsonify, current_app
from .user_controller import user_by_auth
from jwt import decode, encode
import jwt
from json import dumps
from werkzeug.security import check_password_hash


"""def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message': 'O token está em falta', 'data': []}), 401
        try:
            print(token)
            data = decode(dumps(token), current_app.config['SECRET_KEY'])
            current_user = user_by_auth(username=data[0]['username'])
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Signature expired. Please log in again.'}), 400
        except jwt.InvalidTokenError as error:
            return jsonify({'message': 'Invalid token. Please log in again.', 'data': error}), 400
        except:
            return jsonify({'message': 'token invalido ou expirado'}), 400
        return f(current_user, *args, **kwargs)

    return decorated


# Gerando token com base na Secret key do app e definindo expiração com 'exp'
def auth():
    auth = [request.json['email'], request.json['password']]
    check_credential_exits(auth[0], auth[1])
    user = user_by_auth(auth[0])
    if not user:
        return jsonify({'status': 400,'message': 'Este usuario não existe, por favor efetue o registro!'})

    if user and check_password_hash(user.password, auth[1]):
        playload = {
           'username': user.fisrtName, 
           'exp': datetime.datetime.now() + datetime.timedelta(hours=12)
        }
        token = encode(playload, current_app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({'message': 'Validated successfully', 'token': token,
                        'exp': datetime.datetime.now() + datetime.timedelta(hours=12)})
    return jsonify({'status': 400, 'message': 'Senha invalida!'})


def check_credential_exits(email, password):
    if not email or not password:
        return jsonify({'status': 400, 'message': 'Informe o email e a senha para efetuar o login!'})

"""