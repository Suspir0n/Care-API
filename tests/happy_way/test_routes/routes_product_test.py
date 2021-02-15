def test_post_product(app, client):
    mock_request_data = {
        "user_fk": "a9b53c5a-e5e8-420a-91b7-6793259e349e",
        "sub_category_fk": "22265d14-d9b9-408b-994e-05ef5cf15bed",
        "name": "Cadeira Pet",
        "description": "cadeira feita de garrafa pet",
        "value": "R$ 25,99",
        "photo": ""
    }
    response = client.post('/products', json=mock_request_data)
    assert response.status_code == 201
    expected = 'successfully registered'
    assert expected in response.get_data(as_text=True)

def test_get_products(app, client):
    response = client.get('/products')
    assert response.status_code == 200
    expected = 'successfully fetched'
    assert expected in response.get_data(as_text=True)


def test_get_product_by_id(app, client):
    response = client.get('/products/458b3e6b-32ad-4d06-8da4-66a59908ced9')
    assert response.status_code == 201
    expected = 'successfully fetched'
    assert expected in response.get_data(as_text=True)


def test_update_product(app, client):
    mock_request_data = {
        "user_fk": "029e8c67-b750-4f59-8980-bdfc07895fbd",
        "sub_category_fk": "22265d14-d9b9-408b-994e-05ef5cf15bed",
        "name": "teste",
        "description": "teste rodando",
        "value": "999,99"
    }
    response = client.put('/products/458b3e6b-32ad-4d06-8da4-66a59908ced9', json=mock_request_data)
    assert response.status_code == 201
    expected = 'successfully updated'
    assert expected in response.get_data(as_text=True)


def test_delete_product(app, client):
    response = client.delete('/products/e59999a5-ba37-4e05-9b06-18ca88c3ffce')
    assert response.status_code == 404
    expected = 'product dont exist'
    assert expected in response.get_data(as_text=True)