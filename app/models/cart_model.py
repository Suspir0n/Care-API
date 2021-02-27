import datetime
import uuid
from sqlalchemy import ForeignKey
from sqlalchemy.orm import backref
from ..settings.config import db


class CartModel(db.Model):
    __tablename__ = 'cart'
    uid = db.Column(db.String, primary_key=True, default=uuid.uuid4(), unique=True)
    active = db.Column(db.Boolean, default=True)
    deleted = db.Column(db.Boolean, default=False)
    createAt = db.Column(db.DateTime, default=datetime.datetime.now())
    updateAt = db.Column(db.DateTime, default=datetime.datetime.now())
    product_fk = db.Column(db.String, ForeignKey('product.uid'))
    product = db.relationship('NewProductModel', backref=backref('cart', uselist=False))
    address_fk = db.Column(db.String, ForeignKey('address.uid'))
    address = db.relationship('AddressModel', backref=backref('cart', uselist=False))
    card_fk = db.Column(db.String, ForeignKey('card.uid'))
    card = db.relationship('CardModel', backref=backref('cart', uselist=False))


    def __init__(self, productFK, addressFK, cardFK):
        self.product_fk = productFK
        self.address_fk = addressFK
        self.card_fk = cardFK
