import datetime
from werkzeug.security import generate_password_hash
from flask import current_app, request, jsonify
from ..models.user_model import UserModel
from ..schemas.user_serealize import user_schema, users_schema


def get_users():
    users = UserModel.query.all()
    if users:
        result = users_schema.dump(users)
        return jsonify({'message': 'successfully fetched', 'data': result}), 200

    return jsonify({'message': 'user dont exist', 'data': {}}), 404


def get_user(uid):
    user = UserModel.query.get(uid)
    if user:
        result = user_schema.dump(user)
        return jsonify({'message': 'successfully fetched', 'data': result}), 201

    return jsonify({'message': 'user dont exist', 'data': {}}), 404


def delete_user(uid):
    user = UserModel.query.get(uid)
    if not user:
        return jsonify({'message': 'user dont exist', 'data': {}}), 404
    if user:
        try:
            current_app.db.session.delete(user)
            current_app.db.session.commit()
            result = user_schema.dump(user)
            return jsonify({'message': 'successfully deleted', 'data': result}), 200
        except Exception as error:
            return jsonify({'message': 'unable to delete', 'data': {}}), 500



def update_user(uid):
    fisrtName = request.json['first_name']
    lastName = request.json['last_name']
    email = request.json['email']
    password = request.json['password']
    user = UserModel.query.get(uid)

    if not user:
        return jsonify({'message': "user don't exist", 'data': {}}), 404

    pass_hash = generate_password_hash(password)

    if user:
        try:
            user.update = datetime.datetime.now()
            user.fisrtName = fisrtName
            user.lastName = lastName
            user.email = email
            user.password = pass_hash
            current_app.db.session.commit()
            result = user_schema.dump(user)
            return jsonify({'message': 'successfully updated', 'data': result}), 201
        except Exception as error:
            return jsonify({'message': 'unable to update', 'data': {}}), 500


def post_user():
    fisrtName = request.json['first_name']
    lastName = request.json['last_name']
    email = request.json['email']
    password = request.json['password']
    pass_hash = generate_password_hash(password)
    user = UserModel(fisrtName, lastName, email, pass_hash)
    try:
        current_app.db.session.add(user)
        current_app.db.session.commit()
        result = user_schema.dump(user)
        return jsonify({'message': 'successfully registered', 'data': result}), 201
    except:
        return jsonify({'message': 'unable to create', 'data': {}}), 500