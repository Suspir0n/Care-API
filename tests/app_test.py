def test_app_is_created(app):
    assert app.name == 'care_api.app'

def test_request_returns_404(client):
    assert client.get('/url_not_found').status_code == 404