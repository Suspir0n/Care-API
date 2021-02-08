from ..settings.config import ma


class CategorySchema(ma.Schema):
    class Meta:
        fields = ('uid', 'active', 'deleted', 'createAt', 'updateAt', 'name', 'description')

category_schema = CategorySchema()
categorys_schema = CategorySchema(many=True)