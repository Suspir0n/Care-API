import datetime
import uuid
from sqlalchemy import ForeignKey
from sqlalchemy.orm import backref
from ..settings.config import db


class SubCategoryModel(db.Model):
    __tablename__ = 'sub_category'
    uid = db.Column(db.String, primary_key=True, default=uuid.uuid4, unique=True)
    active = db.Column(db.Boolean, default=True)
    deleted = db.Column(db.Boolean, default=False)
    createAt = db.Column(db.DateTime, default=datetime.datetime.now())
    updateAt = db.Column(db.DateTime, default=datetime.datetime.now())
    category_fk = db.Column(db.String, ForeignKey('category.uid'))
    category = db.relationship('CategoryModel', backref=backref('category', uselist=False))
    name = db.Column(db.String(200), unique=True, nullable=False)
    decription = db.Column(db.String(500), unique=True, nullable=False)

    def __init__(self, categoryFK, name, decription):
        self.category_fk = categoryFK
        self.name = name
        self.description = decription
