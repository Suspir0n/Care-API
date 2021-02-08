from ..settings.config import ma


class CardSchema(ma.Schema):
    class Meta:
        fields = ('uid', 'active', 'deleted', 'createAt', 'updateAt', 'num_card', 'name', 'date_valid', 'cod_security')

card_schema = CardSchema()
cards_schema = CardSchema(many=True)