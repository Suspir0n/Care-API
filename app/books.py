from flask import Blueprint, current_app, request, jsonify
from .model import Book
from .serealizer import BookSchema, books_schema

bp_books = Blueprint('books', __name__)

@bp_books.route('/mostrar', methods=['GET'])
def mostrar():
    bs = BookSchema(many=True)
    books = Book.query.all()
    if books:
        result = books_schema.dump(books)
        return jsonify({'message': 'successfully fetched', 'data': result}), 200

    return jsonify({'message': 'nothing found', 'data': {}}), 400


@bp_books.route('/deletar/<id>', methods=['GET'])
def deletar(id):
    Book.query.filter(Book.id == id).delete()
    current_app.db.session.commit()
    return jsonify('Deletado!!!'), 201



@bp_books.route('/modificar/<id>', methods=['POST'])
def modificar(id):
    bs = BookSchema()
    query = Book.query.filter(Book.id == id)
    query.update(request.json)
    current_app.db.session.commit()
    return bs.jsonify(query.first())

@bp_books.route('/cadastrar', methods=['POST'])
def cadastrar():
    bs = BookSchema()
    escritor = request.json['escritor']
    livro = request.json['livro']
    book = Book(escritor, livro)
    """try:
        db.session.add()
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify({'message': 'successfully registered', 'data': result}), 201
    except:
        return jsonify({'message': 'unable to create', 'data': {}}), 500
    d = {'escritor': request.json['escritor'], 'livro': request.json['livro']}
    book, error = bs.load(d)"""
    current_app.db.session.add(book)
    current_app.db.session.commit()
    result = bs.dump(book)
    return jsonify({'message': 'successfully fetched', 'data': result}), 201
