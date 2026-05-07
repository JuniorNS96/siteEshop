from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from app.schemas.produtos import produto_response
from app.schemas.usuario import UserDB, UserPublic, UserSchema

app = FastAPI(
    title='Minha API de estudos',
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
