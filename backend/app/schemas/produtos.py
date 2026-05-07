from pydantic import BaseModel


class produto_preco(BaseModel):
    valor_padrao: int
    valor_com_desconto: int


class produto_response(BaseModel):
    id: int
    nome: str
    preco: produto_preco
