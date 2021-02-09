from flask import Blueprint
from ..controllers import sub_category_controller

bp_sub_category = Blueprint('sub_categorys', __name__)

@bp_sub_category.route('/sub_categorys', methods=['GET'])
def get_sub_categorys():
    return sub_category_controller.get_sub_categorys()


@bp_sub_category.route('/sub_categorys/<uid>', methods=['GET'])
def get_sub_category(uid):
    return sub_category_controller.get_sub_category(uid)


@bp_sub_category.route('/sub_categorys', methods=['POST'])
def post_sub_category():
    return sub_category_controller.post_sub_category()


@bp_sub_category.route('/sub_categorys/<uid>', methods=['DELETE'])
def delete_sub_category(uid):
    return sub_category_controller.delete_sub_category(uid)


@bp_sub_category.route('/sub_categorys/<uid>', methods=['PUT'])
def update_sub_category(uid):
    return sub_category_controller.update_sub_category(uid)
