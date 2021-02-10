def test_post_sub_category(app, client):
    mock_request_data = {
        "category_fk": "47314685-54c1-4863-9918-09f58b981eea",
        "name": "teste",
        "description": "testado testando"
    }
    response = client.post('/sub_categorys', json=mock_request_data)
    assert response.status_code == 201
    expected = 'successfully registered'
    assert expected in response.get_data(as_text=True)

def test_get_sub_categorys(app, client):
    response = client.get('/sub_categorys')
    assert response.status_code == 200
    expected = 'successfully fetched'
    assert expected in response.get_data(as_text=True)


def test_get_sub_category_by_id(app, client):
    response = client.get('/sub_categorys/d61829b1-3e6b-4cc5-83d4-8381b71a613c')
    assert response.status_code == 201
    expected = 'successfully fetched'
    assert expected in response.get_data(as_text=True)


def test_update_sub_catgeory(app, client):
    mock_request_data = {
        "category_fk": "47314685-54c1-4863-9918-09f58b981eea",
        "name": "teste update",
        "description": "update com sucesso"
    }
    response = client.put('/sub_categorys/d61829b1-3e6b-4cc5-83d4-8381b71a613c', json=mock_request_data)
    assert response.status_code == 201
    expected = 'successfully updated'
    assert expected in response.get_data(as_text=True)


def test_delete_sub_catgeory(app, client):
    response = client.delete('/sub_categorys/e59999a5-ba37-4e05-9b06-18ca88c3ffce')
    assert response.status_code == 404
    expected = 'sub category dont exist'
    assert expected in response.get_data(as_text=True)