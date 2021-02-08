import datetime
from flask import current_app, request, jsonify
from ..models.address_model import AddressModel
from ..schemas.address_serealize import address_schema, addresss_schema


def get_addresss():
    addresss = AddressModel.query.all()
    if addresss:
        result = addresss_schema.dump(addresss)
        return jsonify({'message': 'successfully fetched', 'data': result}), 200

    return jsonify({'message': 'address dont exist', 'data': {}}), 404


def get_address(uid):
    address = AddressModel.query.get(uid)
    if address:
        result = address_schema.dump(address)
        return jsonify({'message': 'successfully fetched', 'data': result}), 201

    return jsonify({'message': 'address dont exist', 'data': {}}), 404


def delete_address(uid):
    address = AddressModel.query.get(uid)
    if not address:
        return jsonify({'message': 'address dont exist', 'data': {}}), 404
    if address:
        try:
            current_app.db.session.delete(address)
            current_app.db.session.commit()
            result = address_schema.dump(address)
            return jsonify({'message': 'successfully deleted', 'data': result}), 200
        except Exception as error:
            return jsonify({'message': 'unable to delete', 'data': {}}), 500



def update_address(uid):
    user_fk = request.json['user_fk']
    address = request.json['address']
    address_complementation = request.json['address_complementation']
    state = request.json['state']
    city = request.json['city']
    zipcode = request.json['zipcode']
    phone = request.json['phone']
    _address = AddressModel.query.get(uid)

    if not _address:
        return jsonify({'message': "address don't exist", 'data': {}}), 404
    if _address:
        try:
            _address.update = datetime.datetime.now()
            _address.user_fk = user_fk
            _address.address = address
            _address.address_complementation = address_complementation
            _address.state = state
            _address.city = city
            _address.zipcode = zipcode
            _address.phone = phone
            current_app.db.session.commit()
            result = address_schema.dump(_address)
            return jsonify({'message': 'successfully updated', 'data': result}), 201
        except Exception as error:
            return jsonify({'message': 'unable to update', 'data': {}}), 500


def post_address():
    user_fk = request.json['user_fk']
    address = request.json['address']
    address_complementation = request.json['address_complementation']
    state = request.json['state']
    city = request.json['city']
    zipcode = request.json['zipcode']
    phone = request.json['phone']
    _address = AddressModel(user_fk, address, address_complementation, state, city, zipcode, phone)
    try:
        current_app.db.session.add(_address)
        current_app.db.session.commit()
        result = address_schema.dump(_address)
        return jsonify({'message': 'successfully registered', 'data': result}), 201
    except:
        return jsonify({'message': 'unable to create', 'data': {}}), 500