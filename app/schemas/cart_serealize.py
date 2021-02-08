from ..settings.config import ma


class CartSchema(ma.Schema):
    class Meta:
        fields = ('uid', 'active', 'deleted', 'createAt', 'updateAt', 'product_fk', 'address_fk', 'card_fk')

cart_schema = CartSchema()
carts_schema = CartSchema(many=True)