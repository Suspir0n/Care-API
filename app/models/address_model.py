import datetime
import uuid
from sqlalchemy import ForeignKey
from sqlalchemy.orm import backref
from ..settings.config import db


class AddressModel(db.Model):
    __tablename__ = 'address'
    uid = db.Column(db.String, primary_key=True, default=uuid.uuid4, unique=True)
    active = db.Column(db.Boolean, default=True)
    deleted = db.Column(db.Boolean, default=False)
    createAt = db.Column(db.DateTime, default=datetime.datetime.now())
    updateAt = db.Column(db.DateTime, default=datetime.datetime.now())
    user_fk = db.Column(db.String, ForeignKey('user.uid'))
    user = db.relationship('UserModel', backref=backref('user', uselist=False))
    address = db.Column(db.String(100), unique=True, nullable=False)
    address_complementation = db.Column(db.String(1000), unique=True, nullable=False)
    state = db.Column(db.String(2), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    zipcode = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(50), nullable=False)

    def __init__(self, userFK, address, address_complementation, state, city, zipcode, phone):
        self.user_fk = userFK
        self.address = address
        self.address_complementation = address_complementation
        self.state = state
        self.city = city
        self.zipcode = zipcode
        self.phone = phone
