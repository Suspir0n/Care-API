from flask import Blueprint
from ..controllers import category_controller

bp_category = Blueprint('categorys', __name__)

@bp_category.route('/categorys', methods=['GET'])
def get_categorys():
    return category_controller.get_categorys()


@bp_category.route('/categorys/<uid>', methods=['GET'])
def get_category(uid):
    return category_controller.get_category(uid)


@bp_category.route('/categorys', methods=['POST'])
def post_category():
    return category_controller.post_category()


@bp_category.route('/categorys/<uid>', methods=['DELETE'])
def delete_category(uid):
    return category_controller.delete_category(uid)


@bp_category.route('/categorys/<uid>', methods=['PUT'])
def update_category(uid):
    return category_controller.update_category(uid)
