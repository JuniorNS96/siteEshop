from pydantic import BaseModel, EmailStr


class UserDefault(BaseModel):
    username: str
    nome: str
    email: EmailStr


class UserSchema(UserDefault):
    senha: str


class UserPublic(UserDefault):
    id: int


class UserDB(UserSchema):
    id: int
