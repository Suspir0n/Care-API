import datetime
import uuid
from ..settings.config import db


class CategoryModel(db.Model):
    __tablename__ = 'category'
    uid = db.Column(db.String, primary_key=True, default=uuid.uuid4, unique=True)
    active = db.Column(db.Boolean, default=True)
    deleted = db.Column(db.Boolean, default=False)
    createAt = db.Column(db.DateTime, default=datetime.datetime.now())
    updateAt = db.Column(db.DateTime, default=datetime.datetime.now())
    name = db.Column(db.String(200), unique=True, nullable=False)
    description = db.Column(db.String(500), unique=True, nullable=False)


    def __init__(self, name, description):
        self.name = name
        self.description = description
