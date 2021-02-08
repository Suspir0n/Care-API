from ..settings.config import ma


class SubCategorySchema(ma.Schema):
    class Meta:
        fields = ('uid', 'active', 'deleted', 'createAt', 'updateAt', 'category_fk', 'name', 'description')

sub_category_schema = SubCategorySchema()
sub_categorys_schema = SubCategorySchema(many=True)