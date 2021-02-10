import datetime
from functools import wraps
from flask import request, jsonify, current_app
from .user_controller import user_by_username
from jwt import decode, encode
from werkzeug.security import check_password_hash


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message': 'token is missing', 'data': []}), 401
        try:
            data = decode(token, current_app.config['SECRET_KEY'])
            current_user = user_by_username(username=data['username'])
        except:
            return jsonify({'message': 'token is invalid or expired', 'data': []}), 401
        return f(current_user, *args, **kwargs)

    return decorated


# Gerando token com base na Secret key do app e definindo expiração com 'exp'
def auth():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'could not verify', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401
    user = user_by_username(auth.username)
    if not user:
        return jsonify({'message': 'user not found', 'data': []}), 401

    if user and check_password_hash(user.password, auth.password):
        token = encode({'username': user.fisrtName, 'exp': datetime.datetime.now() + datetime.timedelta(hours=12)},
                           current_app.config['SECRET_KEY'])
        return jsonify({'message': 'Validated successfully', 'token': token,
                        'exp': datetime.datetime.now() + datetime.timedelta(hours=12)})

    return jsonify({'message': 'could not verify', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401

