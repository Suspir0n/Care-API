import datetime
from werkzeug.security import generate_password_hash
from flask import current_app, request, jsonify
from ..models.new_product_model import NewProductModel
from ..schemas.new_product_serealize import product_schema, products_schema


def get_products():
    products = NewProductModel.query.all()
    if products:
        result = products_schema.dump(products)
        return jsonify({'message': 'successfully fetched', 'data': result}), 200

    return jsonify({'message': 'product dont exist', 'data': {}}), 404


def get_product(uid):
    product = NewProductModel.query.get(uid)
    if product:
        result = product_schema.dump(product)
        return jsonify({'message': 'successfully fetched', 'data': result}), 201

    return jsonify({'message': 'product dont exist', 'data': {}}), 404


def delete_product(uid):
    product = NewProductModel.query.get(uid)
    if not product:
        return jsonify({'message': 'product dont exist', 'data': {}}), 404
    if product:
        try:
            current_app.db.session.delete(product)
            current_app.db.session.commit()
            result = product_schema.dump(product)
            return jsonify({'message': 'successfully deleted', 'data': result}), 200
        except Exception as error:
            return jsonify({'message': 'unable to delete', 'data': {}}), 500



def update_product(uid):
    user_fk = request.json['user_fk']
    sub_category_fk = request.json['sub_category_fk']
    name = request.json['name']
    description = request.json['description']
    value = request.json['value']
    product = NewProductModel.query.get(uid)

    if not product:
        return jsonify({'message': "product don't exist", 'data': {}}), 404
    if product:
        try:
            product.update = datetime.datetime.now()
            product.user_fk = user_fk
            product.sub_category_fk = sub_category_fk
            product.name = name
            product.description = description
            product.value = value
            current_app.db.session.commit()
            result = product_schema.dump(product)
            return jsonify({'message': 'successfully updated', 'data': result}), 201
        except Exception as error:
            return jsonify({'message': 'unable to update', 'data': {}}), 500


def post_product():
    user_fk = request.json['user_fk']
    sub_category_fk = request.json['sub_category_fk']
    name = request.json['name']
    description = request.json['description']
    value = request.json['value']
    product = NewProductModel(user_fk, sub_category_fk, name, description, value)
    try:
        current_app.db.session.add(product)
        current_app.db.session.commit()
        result = product_schema.dump(product)
        return jsonify({'message': 'successfully registered', 'data': result}), 201
    except:
        return jsonify({'message': 'unable to create', 'data': {}}), 500