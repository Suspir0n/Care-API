from src.entitys.BaseEntitys import BaseEntitys
from src import init_db

database = init_db()


class UserEntitys(database['SQLAlchemy'].Model):
    __tablename__ = 'user'
    firstName = database['SQLAlchemy'].Column(database['SQLAlchemy'].String(100), nullable=False)
    lastName = database['SQLAlchemy'].Column(database['SQLAlchemy'].String(100), nullable=False)
    email = database['SQLAlchemy'].Column(database['SQLAlchemy'].String(200), nullable=False)
    password = database['SQLAlchemy'].Column(database['SQLAlchemy'].String(100), nullable=False)
    photo = database['SQLAlchemy'].Column(database['SQLAlchemy'].String(200), nullable=False)
    isRoot = database['SQLAlchemy'].Column(database['SQLAlchemy'].Boolean, default=False)

    def create(self):
        database['SQLAlchemy'].session.add(self)
        database['SQLAlchemy'].commit()


    def __init__(self, firstName, lastName, email, password, photo, isRoot):
        self.uid = BaseEntitys.uid
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.photo = photo
        self.isRoot = isRoot


    def __repr__(self):
        return '' % self.uid


database['SQLAlchemy'].create_all()