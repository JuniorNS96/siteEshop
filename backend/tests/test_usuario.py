from http import HTTPStatus


def test_user_api_is_working(client):
    response = client.post(
        '/usuarios/',
        json={
            'username': 'JuniorNS',
            'nome': 'Junior Nunes',
            'email': 'junior@gmail.com',
            'senha': 'nao_e_minha_senha',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'JuniorNS',
        'nome': 'Junior Nunes',
        'email': 'junior@gmail.com',
    }


def test_read_usuarios_list(client):
    response = client.get('/usuarios/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'JuniorNS',
                'nome': 'Junior Nunes',
                'email': 'junior@gmail.com',
            }
        ]
    }


def test_update_usuario(client):
    response = client.put(
        '/usuarios/1',
        json={
            'username': 'JuinoNXS',
            'nome': 'Nunes',
            'email': 'nunes@teste.com',
            'senha': 'nao_e_minha_senha',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'JuinoNXS',
        'nome': 'Nunes',
        'email': 'nunes@teste.com',
    }


def test_update_usuario_not_found(client):
    response = client.put(
        '/usuarios/999',
        json={
            'username': 'JuinoNXS',
            'nome': 'Nunes',
            'email': 'nunes@teste.com',
            'senha': 'nao_e_minha_senha',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Usuário não encontrado'}


def test_read_usuario(client):
    response = client.get('/usuarios/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'JuinoNXS',
        'nome': 'Nunes',
        'email': 'nunes@teste.com',
    }


def test_read_usuario_not_found(client):
    response = client.get('/usuarios/-1')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Usuário não encontrado'}


def test_delete_usuario(client):
    response = client.delete('/usuarios/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'JuinoNXS',
        'nome': 'Nunes',
        'email': 'nunes@teste.com',
    }


def test_delete_usuario_not_found(client):
    response = client.delete('/usuarios/-1')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Usuário não encontrado'}
