from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_boas_vindas_api_is_working(client):
    response = client.get('/boas_vindas')
    assert response.status_code == HTTPStatus.OK


def test_boas_vindas_msg_home(client):
    response = client.get('/boas_vindas')
    assert (
        response.text
        == """
    <html>
        <head>
            <title>Minha API</title>
        </head>
        <body>
            <h1>Bem-vindo à minha API!</h1>
            <p>Esta é a página inicial da minha API.</p>
        </body>
    </html>
    """
    )


def test_home_api_is_working(client):
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK


def test_home_msg_ola_mundo(client):
    response = client.get('/')
    assert response.json() == {'msg': 'Olá, Mundo!'}


def test_produtos_retorna_lista(client):
    response = client.get('/produtos')
    assert isinstance(response.json(), list)
