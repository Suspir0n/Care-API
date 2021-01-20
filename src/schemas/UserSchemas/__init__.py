from src import init_db

database = init_db()


class UserSchema(database['Marshmallow'].Schema):
    class Meta:
        fields = ('uid', 'active', 'deleted', 'createAt', 'updateAt', 'firstName', 'lastName', 'email', 'password', 'photo', 'isRoot')


user_schema = UserSchema()
user_schemas = UserSchema(many=True)