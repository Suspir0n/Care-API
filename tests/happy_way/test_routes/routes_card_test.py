def test_post_card(app, client):
    mock_request_data = {
        "num_card": "9999 9999 9999 9999",
        "name": "teste testado teste",
        "date_valid": "09/29",
        "cod_security": "999"
    }
    response = client.post('/cards', json=mock_request_data)
    assert response.status_code == 201
    expected = 'successfully registered'
    assert expected in response.get_data(as_text=True)

def test_get_cards(app, client):
    response = client.get('/cards')
    assert response.status_code == 200
    expected = 'successfully fetched'
    assert expected in response.get_data(as_text=True)


def test_get_card_by_id(app, client):
    response = client.get('/cards/013666f0-0a66-4443-aaba-1923a58a69f3')
    assert response.status_code == 201
    expected = 'successfully fetched'
    assert expected in response.get_data(as_text=True)


def test_update_card(app, client):
    mock_request_data = {
        "num_card": "9999 9999 9999 9999",
        "name": "teste testado teste update",
        "date_valid": "09/29",
        "cod_security": "999"
    }
    response = client.put('/cards/013666f0-0a66-4443-aaba-1923a58a69f3', json=mock_request_data)
    assert response.status_code == 201
    expected = 'successfully updated'
    assert expected in response.get_data(as_text=True)


def test_delete_card(app, client):
    response = client.delete('/cards/e59999a5-ba37-4e05-9b06-18ca88c3ffce')
    assert response.status_code == 404
    expected = 'card dont exist'
    assert expected in response.get_data(as_text=True)