import pytest
from ..app import create_app


@pytest.fixture(scope='module')
def app():
    """
    Instance of main flask app
    :return: app
    """
    return create_app()

@pytest.fixture(scope='module')
def client(app):
    """
    Instance of test_client()
    :param app: receive a instance of main flask app
    :return: test_client()
    """
    return app.test_client()