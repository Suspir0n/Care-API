from src.notification import BaseNotification
from flask import request, jsonify


class BaseController:
    _repository = ''
    _onlyRootController = False
    errorRoot = {'status': 401, 'errors': 'Do you are not authorized to perform this functionality.'}


    def __init__(self, entity, onlyRoot=False):
        self._repository = entity
        self._onlyRootController = onlyRoot


    def check_not_permission(self, req=request):
        try:
            if self._onlyRootController and not req.IsRoot:
                return jsonify({'message': self.errorRoot['errors'], 'data': {}}), self.errorRoot['status']
        except Exception as error:
            return jsonify({'message': 'Welcome Mr. adm', 'data': {}}), 200


    async def get_all(self, req=request, message=''):
        try:
            self.check_not_permission(req) is True
            if self._repository['deleted'] is False:
                return self._repository.query.all()
        except Exception as error:
            return jsonify({'message': message, 'data': {}}), 404


    async def get_one(self, req=request, message=''):
        try:
            self.check_not_permission(req) is True
            uid = str(req.params.id)
            if uid not in '':
                return self._repository.query.get(uid)
        except Exception as errors:
            return jsonify({'message': message, 'data': {}}), 404


    async def post(self, req=request, message='', model=dict(), ignore_permissions=False):
        try:
            if not ignore_permissions:
                self.check_not_permission(self) is True
            return self._repository
        except Exception as errors:
            return jsonify({'message': 'unable to create', 'data': {}}), 500


    async def remove(self, req=request, message=''):
        try:
            self.check_not_permission(self) is True
            uid = str(req.params.id)
            model = await self._repository.get(uid)
            if model is True:
                model['deleted'] = True
                return self._repository
        except Exception as errors:
            return jsonify({'message': 'unable to delete', 'data': {}}), 404








