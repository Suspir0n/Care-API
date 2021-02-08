from ..settings.config import ma


class NewProductSchema(ma.Schema):
    class Meta:
        fields = ('uid', 'active', 'deleted', 'createAt', 'updateAt', 'user_fk', 'sub_category_fk', 'name', 'description', 'value')

product_schema = NewProductSchema()
products_schema = NewProductSchema(many=True)