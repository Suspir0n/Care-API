from flask import Blueprint
from ..controllers import new_product_controller

bp_product = Blueprint('products', __name__)

@bp_product.route('/products', methods=['GET'])
def get_products():
    return new_product_controller.get_products()


@bp_product.route('/products/<uid>', methods=['GET'])
def get_product(uid):
    return new_product_controller.get_product(uid)


@bp_product.route('/products', methods=['POST'])
def post_product():
    return new_product_controller.post_product()


@bp_product.route('/products/<uid>', methods=['DELETE'])
def delete_product(uid):
    return new_product_controller.delete_product(uid)


@bp_product.route('/products/<uid>', methods=['PUT'])
def update_product(uid):
    return new_product_controller.update_product(uid)
