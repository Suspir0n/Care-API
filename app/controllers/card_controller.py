import datetime
from flask import request, jsonify
from ..models.card_model import CardModel
from ..schemas.card_serealize import card_schema, cards_schema
from .base_controller import get_all, get_one, delete, post, update


def get_cards():
    return get_all(CardModel, cards_schema, 'card')


def get_card(uid):
    return get_one(uid, CardModel, card_schema, 'card')


def delete_card(uid):
    return delete(uid, CardModel, card_schema, 'card')


def update_card(uid):
    card = gut_fields(uid)
    return update(card_schema, card['update'], 'card')


def post_card():
    card = gut_fields()
    return post(card_schema, card['post'])


def gut_fields(uid=''):
    num_card = request.json['num_card']
    name = request.json['name']
    date_valid = request.json['date_valid']
    cod_security = request.json['cod_security']
    card_post = CardModel(num_card, name, date_valid, cod_security)
    card_update = passed_data_fields_model(uid, num_card, name, date_valid, cod_security)
    data = {'post': card_post, 'update': card_update}
    return data


def passed_data_fields_model(uid, num_card, name, date_valid, cod_security):
    card = CardModel.query.get(uid)
    if not card:
        return jsonify({'message': "card don't exist", 'data': {}}), 404
    card.update = datetime.datetime.now()
    card.num_card = num_card
    card.name = name
    card.date_valid = date_valid
    card.cod_security = cod_security
    return card