def test_post_user(app, client):
    mock_request_data = {
        "first_name": "Teste",
        "last_name": "Testando",
        "email": "teste@gmail.com",
        "password": "senhaTeste"
    }

    response = client.post('/users', json=mock_request_data)
    assert response.status_code == 201
    expected = 'successfully registered'
    assert expected in response.get_data(as_text=True)


def test_get_users(app, client):
    response = client.get('/users')
    assert response.status_code == 200
    expected = 'successfully fetched'
    assert expected in response.get_data(as_text=True)


def test_get_user_by_id(app, client):
    response = client.get('/users/6e6fe41f-1efb-4770-a0ba-818f358f35a4')
    assert response.status_code == 201
    expected = 'successfully fetched'
    assert expected in response.get_data(as_text=True)


def test_update_user(app, client):
    mock_request_data = {
        "first_name": "Teste updated",
        "last_name": "userteste",
        "email": "teste_updated@gmail.com",
        "password": "senhaTeste"
    }

    response = client.put('/users/6e6fe41f-1efb-4770-a0ba-818f358f35a4', json=mock_request_data)
    assert response.status_code == 201
    expected = 'successfully updated'
    assert expected in response.get_data(as_text=True)


def test_delete_user(app, client):
    response = client.delete('/users/3')
    assert response.status_code == 404
    expected = 'user dont exist'
    assert expected in response.get_data(as_text=True)