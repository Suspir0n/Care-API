from .settings.config import db


class Book(db.Model):
    __tablename__ = 'Book'
    id = db.Column(db.Integer, primary_key=True)
    escritor = db.Column(db.String(255))
    livro = db.Column(db.String(255))

    def __init__(self, escritor, livro):
        self.escritor = escritor
        self.livro = livro