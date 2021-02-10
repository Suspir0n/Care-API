import datetime
from flask import request, jsonify
from ..models.new_product_model import NewProductModel
from ..schemas.new_product_serealize import product_schema, products_schema
from .base_controller import get_all, get_one, delete, post, update


def get_products():
    return get_all(NewProductModel, products_schema, 'product')


def get_product(uid):
    return get_one(uid, NewProductModel, product_schema, 'product')


def delete_product(uid):
    return delete(uid, NewProductModel, product_schema, 'product')


def update_product(uid):
    product = gut_fields(uid)
    return update(product_schema, product['update'], 'product')


def post_product():
    product = gut_fields()
    return post(product_schema, product['post'])


def gut_fields(uid=''):
    user_fk = request.json['user_fk']
    sub_category_fk = request.json['sub_category_fk']
    name = request.json['name']
    description = request.json['description']
    value = request.json['value']
    product_post = NewProductModel(user_fk, sub_category_fk, name, description, value)
    product_update = passed_data_fields_model(uid, user_fk, sub_category_fk, name, description, value)
    data = {'post': product_post, 'update': product_update}
    return data


def passed_data_fields_model(uid, user_fk, sub_category_fk, name, description, value):
    product = NewProductModel.query.get(uid)
    if not product:
        return jsonify({'message': "product don't exist", 'data': {}}), 404
    product.update = datetime.datetime.now()
    product.user_fk = user_fk
    product.sub_category_fk = sub_category_fk
    product.name = name
    product.description = description
    product.value = value
    return product