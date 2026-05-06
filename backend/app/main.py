from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def home():
    return {'msg': 'API funcionando 🚀'}


@app.get('/produtos')
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


@app.get('/categorias')
def categorias():
    return [
        {'id': 1, 'nome': 'Categoria 1'},
        {'id': 2, 'nome': 'Categoria 2'},
        {'id': 3, 'nome': 'Categoria 3'},
    ]
