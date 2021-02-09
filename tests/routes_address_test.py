def test_post_address(app, client):
    mock_request_data = {
        "user_fk": "6e6fe41f-1efb-4770-a0ba-818f358f35a4",
        "address": "Rua Teste",
        "address_complementation": "andar 71",
        "state": "RJ",
        "city": "Rio de Janeiro",
        "zipcode": "41335-225",
        "phone": "+5571988552233"
    }
    response = client.post('/address', json=mock_request_data)
    assert response.status_code == 201
    expected = 'successfully registered'
    assert expected in response.get_data(as_text=True)

def test_get_addresss(app, client):
    response = client.get('/address')
    assert response.status_code == 200
    expected = 'successfully fetched'
    assert expected in response.get_data(as_text=True)


def test_get_address_by_id(app, client):
    response = client.get('/address/e59999a5-ba37-4e05-9b06-18ca88c3ffce')
    assert response.status_code == 201
    expected = 'successfully fetched'
    assert expected in response.get_data(as_text=True)


def test_update_address(app, client):
    mock_request_data = {
        "user_fk": "6e6fe41f-1efb-4770-a0ba-818f358f35a4",
        "address": "Rua Teste update",
        "address_complementation": "andar 75",
        "state": "RJ",
        "city": "Rio de Janeiro",
        "zipcode": "41335-225",
        "phone": "+5571988552233"
    }
    response = client.put('/address/e59999a5-ba37-4e05-9b06-18ca88c3ffce', json=mock_request_data)
    assert response.status_code == 201
    expected = 'successfully updated'
    assert expected in response.get_data(as_text=True)


def test_delete_address(app, client):
    response = client.delete('/address/e59999a5-ba37-4e05-9b06-18ca88c3ffce')
    assert response.status_code == 200
    expected = 'successfully deleted'
    assert expected in response.get_data(as_text=True)