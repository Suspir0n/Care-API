import datetime
from flask import request, jsonify
from ..models.cart_model import CartModel
from ..schemas.cart_serealize import cart_schema, carts_schema
from .base_controller import get_all, get_one, delete, post, update


def get_carts():
    return get_all(CartModel, carts_schema, 'cart')


def get_cart(uid):
    return get_one(uid, CartModel, cart_schema, 'cart')


def delete_cart(uid):
    return delete(uid, CartModel, cart_schema, 'cart')


def update_cart(uid):
    cart = gut_fields(uid)
    return update(cart_schema, cart['update'], 'cart')


def post_cart():
    cart = gut_fields()
    return post(cart_schema, cart['post'])


def gut_fields(uid=''):
    product_fk = request.json['product_fk']
    address_fk = request.json['address_fk']
    card_fk = request.json['card_fk']
    cart_post = CartModel(product_fk, address_fk, card_fk)
    cart_update = passed_data_fields_model(uid, product_fk, address_fk, card_fk)
    data = {'post': cart_post, 'update': cart_update}
    return data


def passed_data_fields_model(uid, product_fk, address_fk, card_fk):
    cart = CartModel.query.get(uid)
    if not cart:
        return jsonify({'message': "cart don't exist", 'data': {}}), 404
    cart.update = datetime.datetime.now()
    cart.product_fk = product_fk
    cart.address_fk = address_fk
    cart.card_fk = card_fk
    return cart
