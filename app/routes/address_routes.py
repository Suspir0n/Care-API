from flask import Blueprint
from ..controllers import address_controller
from flask_jwt_extended import jwt_required

bp_address = Blueprint('address', __name__)


@bp_address.route('/address', methods=['GET'])
@jwt_required()
def get_addresss():
    return address_controller.get_addresss()


@bp_address.route('/address/<uid>', methods=['GET'])
@jwt_required()
def get_address(uid):
    return address_controller.get_address(uid)


@bp_address.route('/address', methods=['POST'])
@jwt_required()
def post_address():
    return address_controller.post_address()


@bp_address.route('/address/<uid>', methods=['DELETE'])
@jwt_required()
def delete_adress(uid):
    return address_controller.delete_address(uid)


@bp_address.route('/address/<uid>', methods=['PUT'])
@jwt_required()
def update_address(uid):
    return address_controller.update_address(uid)
