import datetime
import uuid
from sqlalchemy import ForeignKey
from sqlalchemy.orm import backref
from ..settings.config import db


class NewProductModel(db.Model):
    __tablename__ = 'product'
    uid = db.Column(db.String, primary_key=True, default=uuid.uuid4, unique=True)
    active = db.Column(db.Boolean, default=True)
    deleted = db.Column(db.Boolean, default=False)
    createAt = db.Column(db.DateTime, default=datetime.datetime.now())
    updateAt = db.Column(db.DateTime, default=datetime.datetime.now())
    user_fk = db.Column(db.String, ForeignKey('user.uid'))
    user = db.relationship('UserModel', backref=backref('user', uselist=False))
    sub_category_fk = db.Column(db.String, ForeignKey('sub_category.uid'))
    sub_category = db.relationship('SubCategoryModel', backref=backref('sub_category', uselist=False))
    name = db.Column(db.String(200), unique=True, nullable=False)
    description = db.Column(db.String(500), unique=True, nullable=False)
    value = db.Column(db.String(10), nullable=False)

    def __init__(self, userFK, sub_categoryFK, name, description, value):
        self.user_fk = userFK
        self.sub_category_fk = sub_categoryFK
        self.name = name
        self.description = description
        self.value = value
