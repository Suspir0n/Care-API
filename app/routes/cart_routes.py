from flask import Blueprint
from ..controllers import cart_controller

bp_cart = Blueprint('carts', __name__)

@bp_cart.route('/carts', methods=['GET'])
def get_carts():
    return cart_controller.get_carts()


@bp_cart.route('/carts/<uid>', methods=['GET'])
def get_cart(uid):
    return cart_controller.get_cart(uid)


@bp_cart.route('/carts', methods=['POST'])
def post_cart():
    return cart_controller.post_cart()


@bp_cart.route('/carts/<uid>', methods=['DELETE'])
def delete_cart(uid):
    return cart_controller.delete_cart(uid)


@bp_cart.route('/carts/<uid>', methods=['PUT'])
def update_cart(uid):
    return cart_controller.update_cart(uid)
