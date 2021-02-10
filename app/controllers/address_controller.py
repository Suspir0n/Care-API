import datetime
from flask import request, jsonify
from ..models.address_model import AddressModel
from ..schemas.address_serealize import address_schema, addresss_schema
from .base_controller import get_all, get_one, delete, post, update


def get_addresss():
    return get_all(AddressModel, addresss_schema, 'address')


def get_address(uid):
    return get_one(uid, AddressModel, address_schema, 'address')


def delete_address(uid):
    return delete(uid, AddressModel, address_schema, 'address')


def update_address(uid):
    address = gut_fields(uid)
    return update(address_schema, address['update'], 'address')


def post_address():
    address = gut_fields()
    return post(address_schema, address['post'])


def gut_fields(uid=''):
    user_fk = request.json['user_fk']
    address = request.json['address']
    address_complementation = request.json['address_complementation']
    state = request.json['state']
    city = request.json['city']
    zipcode = request.json['zipcode']
    phone = request.json['phone']
    _address_post = AddressModel(user_fk, address, address_complementation, state, city, zipcode, phone)
    _address_update = passed_data_fields_model(uid, user_fk, address, address_complementation, state, city, zipcode, phone)
    data = {'post': _address_post, 'update': _address_update}
    return data


def passed_data_fields_model(uid, user_fk, address, address_complementation, state, city, zipcode, phone):
    _address = AddressModel.query.get(uid)
    if not _address:
        return jsonify({'message': "address don't exist", 'data': {}}), 404
    _address.update = datetime.datetime.now()
    _address.user_fk = user_fk
    _address.address = address
    _address.address_complementation = address_complementation
    _address.state = state
    _address.city = city
    _address.zipcode = zipcode
    _address.phone = phone
    return _address