from flask import Blueprint
from ..controllers import card_controller

bp_card = Blueprint('cards', __name__)

@bp_card.route('/cards', methods=['GET'])
def get_cards():
    return card_controller.get_cards()


@bp_card.route('/cards/<uid>', methods=['GET'])
def get_card(uid):
    return card_controller.get_card(uid)


@bp_card.route('/cards', methods=['POST'])
def post_card():
    return card_controller.post_card()


@bp_card.route('/cards/<uid>', methods=['DELETE'])
def delete_card(uid):
    return card_controller.delete_card(uid)


@bp_card.route('/cards/<uid>', methods=['PUT'])
def update_card(uid):
    return card_controller.update_card(uid)
