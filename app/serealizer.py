from .settings.config import ma

class BookSchema(ma.Schema):
    class Meta:
        fields = ('id', 'escritor', 'livro')

book_schema = BookSchema()
books_schema = BookSchema(many=True)