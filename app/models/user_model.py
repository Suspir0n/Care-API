import datetime
import uuid
from ..settings.config import db


class UserModel(db.Model):
    __tablename__ = 'user'
    uid = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()), unique=True)
    active = db.Column(db.Boolean, default=True)
    deleted = db.Column(db.Boolean, default=False)
    createAt = db.Column(db.DateTime, default=datetime.datetime.now())
    updateAt = db.Column(db.DateTime, default=datetime.datetime.now())
    fisrtName = db.Column(db.String(20), unique=True, nullable=False)
    lastName = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)


    def __init__(self, firstName, lastName, email, password):
        self.fisrtName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
