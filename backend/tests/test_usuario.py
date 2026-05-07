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
