import datetime
from flask import request, jsonify
from ..models.sub_category_model import SubCategoryModel
from ..schemas.sub_category_serealize import sub_category_schema, sub_categorys_schema
from .base_controller import get_all, get_one, delete, post, update


def get_sub_categorys():
    return get_all(SubCategoryModel, sub_categorys_schema, 'sub category')


def get_sub_category(uid):
    return get_one(uid, SubCategoryModel, sub_category_schema, 'sub category')


def delete_sub_category(uid):
    return delete(uid, SubCategoryModel, sub_category_schema, 'sub category')


def update_sub_category(uid):
    sub_category = gut_fields(uid)
    return update(sub_category_schema, sub_category['update'], 'sub category')


def post_sub_category():
    sub_category = gut_fields()
    return post(sub_category_schema, sub_category['post'])


def gut_fields(uid=''):
    category_fk = request.json['category_fk']
    name = request.json['name']
    description = request.json['description']
    sub_category_post = SubCategoryModel(category_fk, name, description)
    sub_category_update = passed_data_fields_model(uid, category_fk, name, description)
    data = {'post': sub_category_post, 'update': sub_category_update}
    return data


def passed_data_fields_model(uid, category_fk, name, description):
    sub_category = SubCategoryModel.query.get(uid)
    if not sub_category:
        return jsonify({'message': "sub category don't exist", 'data': {}}), 404
    sub_category.update = datetime.datetime.now()
    sub_category.category_fk = category_fk
    sub_category.name = name
    sub_category.description = description
    return sub_category