import datetime
from flask import current_app, request, jsonify
from ..models.card_model import CardModel
from ..schemas.card_serealize import card_schema, cards_schema


def get_cards():
    cards = CardModel.query.all()
    if cards:
        result = cards_schema.dump(cards)
        return jsonify({'message': 'successfully fetched', 'data': result}), 200

    return jsonify({'message': 'card dont exist', 'data': {}}), 404


def get_card(uid):
    card = CardModel.query.get(uid)
    if card:
        result = card_schema.dump(card)
        return jsonify({'message': 'successfully fetched', 'data': result}), 201

    return jsonify({'message': 'card dont exist', 'data': {}}), 404


def delete_card(uid):
    card = CardModel.query.get(uid)
    if not card:
        return jsonify({'message': 'card dont exist', 'data': {}}), 404
    if card:
        try:
            current_app.db.session.delete(card)
            current_app.db.session.commit()
            result = card_schema.dump(card)
            return jsonify({'message': 'successfully deleted', 'data': result}), 200
        except Exception as error:
            return jsonify({'message': 'unable to delete', 'data': {}}), 500



def update_card(uid):
    num_card = request.json['num_card']
    name = request.json['name']
    date_valid = request.json['date_valid']
    cod_security = request.json['cod_security']
    card = CardModel.query.get(uid)

    if not card:
        return jsonify({'message': "card don't exist", 'data': {}}), 404
    if card:
        try:
            card.update = datetime.datetime.now()
            card.num_card = num_card
            card.name = name
            card.date_valid = date_valid
            card.cod_security = cod_security
            current_app.db.session.commit()
            result = card_schema.dump(card)
            return jsonify({'message': 'successfully updated', 'data': result}), 201
        except Exception as error:
            return jsonify({'message': 'unable to update', 'data': {}}), 500


def post_card():
    num_card = request.json['num_card']
    name = request.json['name']
    date_valid = request.json['date_valid']
    cod_security = request.json['cod_security']
    card = CardModel(num_card, name, date_valid, cod_security)
    try:
        current_app.db.session.add(card)
        current_app.db.session.commit()
        result = card_schema.dump(card)
        return jsonify({'message': 'successfully registered', 'data': result}), 201
    except:
        return jsonify({'message': 'unable to create', 'data': {}}), 500