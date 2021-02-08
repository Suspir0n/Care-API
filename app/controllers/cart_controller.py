import datetime
from flask import current_app, request, jsonify
from ..models.cart_model import CartModel
from ..schemas.cart_serealize import cart_schema, carts_schema


def get_carts():
    carts = CartModel.query.all()
    if carts:
        result = carts_schema.dump(carts)
        return jsonify({'message': 'successfully fetched', 'data': result}), 200

    return jsonify({'message': 'cart dont exist', 'data': {}}), 404


def get_cart(uid):
    cart = CartModel.query.get(uid)
    if cart:
        result = cart_schema.dump(cart)
        return jsonify({'message': 'successfully fetched', 'data': result}), 201

    return jsonify({'message': 'cart dont exist', 'data': {}}), 404


def delete_cart(uid):
    cart = CartModel.query.get(uid)
    if not cart:
        return jsonify({'message': 'cart dont exist', 'data': {}}), 404
    if cart:
        try:
            current_app.db.session.delete(cart)
            current_app.db.session.commit()
            result = cart_schema.dump(cart)
            return jsonify({'message': 'successfully deleted', 'data': result}), 200
        except Exception as error:
            return jsonify({'message': 'unable to delete', 'data': {}}), 500



def update_cart(uid):
    product_fk = request.json['product_fk']
    address_fk = request.json['address_fk']
    card_fk = request.json['card_fk']
    cart = CartModel.query.get(uid)

    if not cart:
        return jsonify({'message': "cart don't exist", 'data': {}}), 404
    if cart:
        try:
            cart.update = datetime.datetime.now()
            cart.product_fk = product_fk
            cart.address_fk = address_fk
            cart.card_fk = card_fk
            current_app.db.session.commit()
            result = cart_schema.dump(cart)
            return jsonify({'message': 'successfully updated', 'data': result}), 201
        except Exception as error:
            return jsonify({'message': 'unable to update', 'data': {}}), 500


def post_cart():
    product_fk = request.json['product_fk']
    address_fk = request.json['address_fk']
    card_fk = request.json['card_fk']
    cart = CartModel(product_fk, address_fk, card_fk)
    try:
        current_app.db.session.add(cart)
        current_app.db.session.commit()
        result = cart_schema.dump(cart)
        return jsonify({'message': 'successfully registered', 'data': result}), 201
    except:
        return jsonify({'message': 'unable to create', 'data': {}}), 500