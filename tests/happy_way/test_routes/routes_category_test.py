def test_post_category(app, client):
    mock_request_data = {
        "name": "Garrafa",
        "description": "feita de garrafa"
    }
    response = client.post('/categorys', json=mock_request_data)
    assert response.status_code == 201
    expected = 'successfully registered'
    assert expected in response.get_data(as_text=True)

def test_get_categorys(app, client):
    response = client.get('/categorys')
    assert response.status_code == 200
    expected = 'successfully fetched'
    assert expected in response.get_data(as_text=True)


def test_get_category_by_id(app, client):
    response = client.get('/categorys/47314685-54c1-4863-9918-09f58b981eea')
    assert response.status_code == 201
    expected = 'successfully fetched'
    assert expected in response.get_data(as_text=True)


def test_update_catgeory(app, client):
    mock_request_data = {
        "name": "cadeira de garrafa teste",
        "description": "feita de garrafa pet e costurada com pano"
    }
    response = client.put('/categorys/47314685-54c1-4863-9918-09f58b981eea', json=mock_request_data)
    assert response.status_code == 201
    expected = 'successfully updated'
    assert expected in response.get_data(as_text=True)


def test_delete_catgeory(app, client):
    response = client.delete('/categorys/e59999a5-ba37-4e05-9b06-18ca88c3ffce')
    assert response.status_code == 404
    expected = 'category dont exist'
    assert expected in response.get_data(as_text=True)