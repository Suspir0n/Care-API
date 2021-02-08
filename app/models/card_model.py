import datetime
import uuid
from ..settings.config import db


class CardModel(db.Model):
    __tablename__ = 'card'
    uid = db.Column(db.String, primary_key=True, default=uuid.uuid4, unique=True)
    active = db.Column(db.Boolean, default=True)
    deleted = db.Column(db.Boolean, default=False)
    createAt = db.Column(db.DateTime, default=datetime.datetime.now())
    updateAt = db.Column(db.DateTime, default=datetime.datetime.now())
    num_card = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(100), unique=True, nullable=False)
    date_valid = db.Column(db.String(10), unique=True, nullable=False)
    cod_security = db.Column(db.Integer(3), unique=True, nullable=False)


    def __init__(self, num_card, name, date_valid, cod_security):
        self.num_card = num_card
        self.name = name
        self.date_valid = date_valid
        self.cod_security = cod_security
