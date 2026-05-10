from http import HTTPStatus

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

from app.schemas.produtos import produto_response
from app.schemas.usuario import (
    UserDB,
    UserList,
    UserPublic,
    UserSchema,
)

app = FastAPI(
    title='BIG API de estudos',
    description='API de estudos para FastAPI',
    version='1.0.0',
)

meu_banco = []


@app.get('/', status_code=HTTPStatus.OK)
def home():
    return {'msg': 'Olá, Mundo!'}


@app.get(
    '/boas_vindas',
    status_code=HTTPStatus.OK,
    response_class=HTMLResponse,
)
def boas_vindas():
    return """
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


@app.get(
    '/produtos',
    status_code=HTTPStatus.OK,
    response_model=list[produto_response],
)
def produtos():
    return [
        {
            'id': 1,
            'nome': 'Produto 1',
            'preco': {
                'valor_padrao': 10.0,
                'valor_com_desconto': 7.0,
            },
        },
        {
            'id': 2,
            'nome': 'Produto 2',
            'preco': {
                'valor_padrao': 20.0,
                'valor_com_desconto': 15.0,
            },
        },
        {
            'id': 3,
            'nome': 'Produto 3',
            'preco': {
                'valor_padrao': 4000.0,
                'valor_com_desconto': 3200.0,
            },
        },
    ]


@app.post(
    '/usuarios/',
    status_code=HTTPStatus.CREATED,
    response_model=UserPublic,
)
def create_usuario(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(meu_banco) + 1)
    meu_banco.append(user_with_id)
    return user_with_id


@app.get(
    '/usuarios/',
    status_code=HTTPStatus.OK,
    response_model=UserList,
)
def read_usuarios():
    return {'users': meu_banco}


@app.put(
    '/usuarios/{user_id}',
    status_code=HTTPStatus.OK,
    response_model=UserPublic,
)
def update_usuario(user_id: int, user: UserSchema):
    if user_id < 1 or user_id > len(meu_banco):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Usuário não encontrado'
        )
    user_with_id = UserDB(**user.model_dump(), id=user_id)
    meu_banco[user_id - 1] = user_with_id
    return user_with_id


@app.delete(
    '/usuarios/{user_id}',
    status_code=HTTPStatus.OK,
    response_model=UserPublic,
)
def delete_usuario(user_id: int):
    if user_id < 1 or user_id > len(meu_banco):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Usuário não encontrado'
        )
    deleted_user = meu_banco.pop(user_id - 1)
    return deleted_user


@app.get(
    '/usuarios/{user_id}',
    # summary='aaaaa',
    # description='bbbbb',
    # response_description='ccccc',
    status_code=HTTPStatus.OK,
    response_model=UserPublic,
)
def read_usuario(user_id: int):

    usuario = next((u for u in meu_banco if u.id == user_id), None)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario
