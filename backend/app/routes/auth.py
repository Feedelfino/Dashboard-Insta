from fastapi import APIRouter                           # importa classe para agrupar rotas
from app.models.auth import UserCreate                 # importa model de cadastro
from app.models.auth import UserLogin                  # importa model de login
from app.services.auth_service import registrar_usuario   # importa função de cadastro
from app.services.auth_service import autenticar_usuario  # importa função de login

roteador_auth = APIRouter()                            # cria o roteador de autenticação


@roteador_auth.post("/auth/register")                  # cria rota de cadastro
async def register(dados: UserCreate):                 # recebe dados do usuário
    return registrar_usuario(dados)                    # chama service de cadastro


@roteador_auth.post("/auth/login")                     # cria rota de login
async def login(dados: UserLogin):                     # recebe credenciais
    return autenticar_usuario(dados)                   # chama service de autenticação