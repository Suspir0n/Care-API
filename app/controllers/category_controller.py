import datetime
from flask import request, jsonify
from ..models.category_model import CategoryModel
from ..schemas.category_serealize import category_schema, categorys_schema
from .base_controller import get_all, get_one, delete, post, update


def get_categorys():
    return get_all(CategoryModel, categorys_schema, 'category')


def get_category(uid):
    return get_one(uid, CategoryModel, category_schema, 'category')


def delete_category(uid):
    return delete(uid, CategoryModel, category_schema, 'category')


def update_category(uid):
    category = gut_fields(uid)
    return update(category_schema, category['update'], 'category')


def post_category():
    category = gut_fields()
    return post(category_schema, category['post'])


def gut_fields(uid=''):
    name = request.json['name']
    description = request.json['description']
    category_post = CategoryModel(name, description)
    category_update = passed_data_fields_model(uid, name, description)
    data = {'post': category_post, 'update': category_update}
    return data


def passed_data_fields_model(uid, name, description):
    category = CategoryModel.query.get(uid)
    if not category:
        return jsonify({'message': "category don't exist", 'data': {}}), 404
    category.update = datetime.datetime.now()
    category.name = name
    category.description = description
    return category