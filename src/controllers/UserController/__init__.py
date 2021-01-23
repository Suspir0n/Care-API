from src.controllers.BaseControllers import BaseController
from src.entitys.UserEntitys import UserEntitys
from src.schemas.UserSchemas import user_schema, user_schemas
from flask import request, jsonify
from _md5 import md5


class UserController(BaseController):
    def __init__(self):
        super(self, UserEntitys)


    def data(self, req=request):
        firstName = req.json['firstName']
        lastName = req.json['lastName']
        email = req.json['email']
        password = req.json['password']
        confirmPassword = req.json['password']
        isRoot = req.json['isRoot']


    def required_fields(self):
        super().is_required(self.data.firstName, 'Enter your first name')
        super().is_required(self.data.lastName, 'Enter your last name')
        super().is_required(self.data.email, 'Enter your e-mail')
        super().is_required(self.data.password, 'Enter your password')
        super().is_required(self.data.confirmPassword, 'Enter your password again')



    def verify_if_passwords_are_differents(self, isTrue):
        if isTrue:
            return jsonify({'message': 'The password and password confirmation are different'}), 400


    def convert_password_to_md5(self, isTrue, _user):
        if isTrue:
            _user.password = md5(self.data.password)


    async def create_user(self):
        self.required_fields(self)
        _user = UserEntitys()
        _user.firstName = self.data.firstName
        _user.lastName = self.data.lastName
        _user.email = self.data.email
        self.verify_if_passwords_are_differents(self, (self.data.password != self.data.confirmPassword))
        self.convert_password_to_md5(self, (self.data.password is True), _user)

        _user.isRoot = self.data.isRoot
        return super().post(_user, user_schema, True)