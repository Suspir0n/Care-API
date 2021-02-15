import datetime
from werkzeug.security import generate_password_hash
from flask import request, jsonify
from ..models.user_model import UserModel
from ..schemas.user_serealize import user_schema, users_schema
from .base_controller import get_all, get_one, delete, post, update
from ..notify.base_notification import is_required 


def get_users():
    return get_all(UserModel, users_schema, 'user')


def get_user(uid):
    return get_one(uid, UserModel, user_schema, 'user')


def delete_user(uid):
    return delete(uid, UserModel, user_schema, 'user')


def update_user(uid):
    user = gut_fields(uid)
    return update(user_schema, user['update'], 'user')


def post_user():
    user = gut_fields()
    return post(user_schema, user['post'])


def validation_fields(fisrtName, lastName, email, password):
    is_required(fisrtName, 'Informe o seu primeiro nome!')
    is_required(lastName, 'Informe o seu sobrenome!')
    is_required(email, 'Informe o seu email!')
    is_required(password, 'Informe a sua senha!')


def gut_fields(uid=''):
    fisrtName = request.json['first_name']
    lastName = request.json['last_name']
    email = request.json['email']
    password = request.json['password']
    pass_hash = generate_password_hash(password)
    validation_fields(fisrtName, lastName, email, password)
    user_update = passed_data_fields_model(uid, fisrtName, lastName, email, password)
    user_post = UserModel(fisrtName, lastName, email, pass_hash)
    data = {'post': user_post, 'update': user_update}
    return data


def passed_data_fields_model(uid, fisrtName, lastName, email, password):
    user = UserModel.query.get(uid)
    if not user:
        return jsonify({'message': "user don't exist", 'data': {}}), 404
    pass_hash = generate_password_hash(password)
    user.update = datetime.datetime.now()
    user.fisrtName = fisrtName
    user.lastName = lastName
    user.email = email
    user.password = pass_hash
    return user


def user_by_auth(email):
    try:
        return UserModel.query.filter(UserModel.email == email).one()
    except:
        return jsonify({'status': 400, 'message': 'Erro de conexão com a banco de dados'})