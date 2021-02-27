from flask import current_app, jsonify


def get_all(model, schemas, name_model):
    data = model.query.all()
    if data:
        result = schemas.dump(data)
        return jsonify({'message': 'successfully fetched', 'data': result}), 200

    return jsonify({'message': f'{name_model} dont exist', 'data': {}}), 404


def get_one(uid, model, schema, name_model):
    data = model.query.get(uid)
    if data:
        result = schema.dump(data)
        return jsonify({'message': 'successfully fetched', 'data': result}), 201

    return jsonify({'message': f'{name_model} dont exist', 'data': {}}), 404


def delete(uid, model, schema, name_model):
    data = model.query.get(uid)
    if not data:
        return jsonify({'message': f'{name_model} dont exist', 'data': {}}), 404
    if data:
        try:
            current_app.db.session.delete(data)
            current_app.db.session.commit()
            result = schema.dump(data)
            return jsonify({'message': 'successfully deleted', 'data': result}), 200
        except Exception as error:
            return jsonify({'message': 'unable to delete', 'data': {}}), 404



def update(schema, data, name_model):
    if not data:
        return jsonify({'message': f"{name_model} don't exist", 'data': {}}), 404
    if data:
        try:
            current_app.db.session.commit()
            result = schema.dump(data)
            return jsonify({'message': 'successfully updated', 'data': result}), 201
        except:
            return jsonify({'message': 'unable to update', 'data': {}}), 404


def post(schema, data):
    try:
        current_app.db.session.add(data)
        current_app.db.session.commit()
        result = schema.dump(data)
        return jsonify({'message': 'successfully registered', 'data': result}), 201
    except Exception as error:
        return jsonify({'message': 'unable to create', 'data': {}, 'error': error}), 500