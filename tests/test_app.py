from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK  # 200
    assert response.json() == {'message': 'Olá Mundo!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'testusername',
            'email': 'test@test.com',
            'password': 'testpassword',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'testusername',
        'email': 'test@test.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {'username': 'testusername', 'email': 'test@test.com', 'id': 1}
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'password': '123',
            'username': 'testusername2',
            'email': 'test@test.com',
            'id': 1,
        },
    )

    assert response.json() == {
        'username': 'testusername2',
        'email': 'test@test.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted successfully'}


def test_update_not_found(client):
    response = client.put(
        '/users/999',
        json={
            'password': '123',
            'username': 'nonexistent',
            'email': 'test@test.com',
            'id': 999,
        },
    )

    assert response.json() == {'detail': 'NOT FOUND'}


def test_delete_not_found(client):
    response = client.delete('/users/999')

    assert response.json() == {'detail': 'NOT FOUND'}


def test_get_user_by_id(client):
    # Cria o usuário antes de buscar
    client.post('/users/', json={
        "username": "testusername2",
        "email": "test@test.com",
        "password": "123"
    })

    # Agora faz o GET
    response = client.get('/users/1')

    assert response.status_code == 200  # noqa: PLR2004
