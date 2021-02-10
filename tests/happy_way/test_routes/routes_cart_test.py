def test_post_cart(app, client):
    mock_request_data = {
        "product_fk": "458b3e6b-32ad-4d06-8da4-66a59908ced9",
        "address_fk": "1e410531-0830-4e62-97cb-e4b3fe20aad0",
        "card_fk": "013666f0-0a66-4443-aaba-1923a58a69f3"
    }
    response = client.post('/carts', json=mock_request_data)
    assert response.status_code == 201
    expected = 'successfully registered'
    assert expected in response.get_data(as_text=True)

def test_get_carts(app, client):
    response = client.get('/carts')
    assert response.status_code == 200
    expected = 'successfully fetched'
    assert expected in response.get_data(as_text=True)


def test_get_cart_by_id(app, client):
    response = client.get('/carts/9512e0b5-5ee9-4823-863d-b34529bd94ea')
    assert response.status_code == 201
    expected = 'successfully fetched'
    assert expected in response.get_data(as_text=True)


def test_update_cart(app, client):
    mock_request_data = {
        "product_fk": "458b3e6b-32ad-4d06-8da4-66a59908ced9",
        "address_fk": "1e410531-0830-4e62-97cb-e4b3fe20aad0",
        "card_fk": "013666f0-0a66-4443-aaba-1923a58a69f3"
    }
    response = client.put('/carts/9512e0b5-5ee9-4823-863d-b34529bd94ea', json=mock_request_data)
    assert response.status_code == 201
    expected = 'successfully updated'
    assert expected in response.get_data(as_text=True)


def test_delete_cart(app, client):
    response = client.delete('/carts/e59999a5-ba37-4e05-9b06-18ca88c3ffce')
    assert response.status_code == 404
    expected = 'cart dont exist'
    assert expected in response.get_data(as_text=True)