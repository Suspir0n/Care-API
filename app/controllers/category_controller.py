import datetime
from flask import current_app, request, jsonify
from ..models.category_model import CategoryModel
from ..schemas.category_serealize import category_schema, categorys_schema


def get_categorys():
    categorys = CategoryModel.query.all()
    if categorys:
        result = categorys_schema.dump(categorys)
        return jsonify({'message': 'successfully fetched', 'data': result}), 200

    return jsonify({'message': 'category dont exist', 'data': {}}), 404


def get_category(uid):
    category = CategoryModel.query.get(uid)
    if category:
        result = category_schema.dump(category)
        return jsonify({'message': 'successfully fetched', 'data': result}), 201

    return jsonify({'message': 'category dont exist', 'data': {}}), 404


def delete_category(uid):
    category = CategoryModel.query.get(uid)
    if not category:
        return jsonify({'message': 'category dont exist', 'data': {}}), 404
    if category:
        try:
            current_app.db.session.delete(category)
            current_app.db.session.commit()
            result = category_schema.dump(category)
            return jsonify({'message': 'successfully deleted', 'data': result}), 200
        except Exception as error:
            return jsonify({'message': 'unable to delete', 'data': {}}), 500



def update_category(uid):
    name = request.json['name']
    description = request.json['description']
    category = CategoryModel.query.get(uid)

    if not category:
        return jsonify({'message': "category don't exist", 'data': {}}), 404
    if category:
        try:
            category.update = datetime.datetime.now()
            category.name = name
            category.description = description
            current_app.db.session.commit()
            result = category_schema.dump(category)
            return jsonify({'message': 'successfully updated', 'data': result}), 201
        except Exception as error:
            return jsonify({'message': 'unable to update', 'data': {}}), 500


def post_category():
    name = request.json['name']
    description = request.json['description']
    category = CategoryModel(name, description)
    try:
        current_app.db.session.add(category)
        current_app.db.session.commit()
        result = category_schema.dump(category)
        return jsonify({'message': 'successfully registered', 'data': result}), 201
    except:
        return jsonify({'message': 'unable to create', 'data': {}}), 500