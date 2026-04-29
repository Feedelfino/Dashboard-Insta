# arquivo responsável por gerar e validar tokens JWT

# usado para definir expiração do token
from datetime import datetime, timedelta
# biblioteca usada para criar e validar JWT
from jose import jwt

# chave secreta usada para assinar o token
SECRET_KEY = "senha_super_secreta"

# algoritmo usado para assinar o token
ALGORITHM = "HS256"

# tempo de validade do token em minutos
ACCESS_TOKEN_EXPIRE_MINUTES = 60


def criar_token(dados: dict):
    # copia os dados do usuário
    payload = dados.copy()

    # calcula o tempo de expiração
    expira = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    # adiciona expiração ao payload
    payload.update({"exp": expira})

    # gera o token assinado
    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    # retorna o token
    return token


def verificar_token(token: str):
    # valida e decodifica o token recebido
    dados = jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM]
    )

    # retorna os dados internos do token
    return dados
