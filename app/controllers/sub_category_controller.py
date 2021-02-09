import datetime
from werkzeug.security import generate_password_hash
from flask import current_app, request, jsonify
from ..models.sub_category_model import SubCategoryModel
from ..schemas.sub_category_serealize import sub_category_schema, sub_categorys_schema


def get_sub_categorys():
    sub_categorys = SubCategoryModel.query.all()
    if sub_categorys:
        result = sub_categorys_schema.dump(sub_categorys)
        return jsonify({'message': 'successfully fetched', 'data': result}), 200

    return jsonify({'message': 'sub category dont exist', 'data': {}}), 404


def get_sub_category(uid):
    sub_category = SubCategoryModel.query.get(uid)
    if sub_category:
        result = sub_category_schema.dump(sub_category)
        return jsonify({'message': 'successfully fetched', 'data': result}), 201

    return jsonify({'message': 'sub category dont exist', 'data': {}}), 404


def delete_sub_category(uid):
    sub_category = SubCategoryModel.query.get(uid)
    if not sub_category:
        return jsonify({'message': 'sub category dont exist', 'data': {}}), 404
    if sub_category:
        try:
            current_app.db.session.delete(sub_category)
            current_app.db.session.commit()
            result = sub_category_schema.dump(sub_category)
            return jsonify({'message': 'successfully deleted', 'data': result}), 200
        except Exception as error:
            return jsonify({'message': 'unable to delete', 'data': {}}), 500



def update_sub_category(uid):
    category_fk = request.json['category_fk']
    name = request.json['name']
    description = request.json['description']
    sub_category = SubCategoryModel.query.get(uid)

    if not sub_category:
        return jsonify({'message': "sub category don't exist", 'data': {}}), 404
    if sub_category:
        try:
            sub_category.update = datetime.datetime.now()
            sub_category.category_fk = category_fk
            sub_category.name = name
            sub_category.description = description
            current_app.db.session.commit()
            result = sub_category_schema.dump(sub_category)
            return jsonify({'message': 'successfully updated', 'data': result}), 201
        except Exception as error:
            return jsonify({'message': 'unable to update', 'data': {}}), 500


def post_sub_category():
    category_fk = request.json['category_fk']
    name = request.json['name']
    description = request.json['description']
    sub_category = SubCategoryModel(category_fk, name, description)
    try:
        current_app.db.session.add(sub_category)
        current_app.db.session.commit()
        result = sub_category_schema.dump(sub_category)
        return jsonify({'message': 'successfully registered', 'data': result}), 201
    except:
        return jsonify({'message': 'unable to create', 'data': {}}), 500