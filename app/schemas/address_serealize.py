from ..settings.config import ma


class AddressSchema(ma.Schema):
    class Meta:
        fields = ('uid', 'active', 'deleted', 'createAt', 'updateAt', 'user_fk', 'address', 'address_complementation', 'state', 'city', 'zipcode', 'phone')

address_schema = AddressSchema()
addresss_schema = AddressSchema(many=True)