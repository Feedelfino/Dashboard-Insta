from pydantic import BaseModel                         # importa a base para criar models Pydantic


class UserCreate(BaseModel):                           # model usado para cadastro de usuário
    nome: str                                          # nome do usuário
    email: str                                         # email do usuário
    senha: str                                         # senha enviada no cadastro


class UserLogin(BaseModel):                            # model usado para login
    email: str                                         # email informado no login
    senha: str                                         # senha informada no login