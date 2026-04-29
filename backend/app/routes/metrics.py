# importa tipagem para listas
from typing import List

# importa recursos do FastAPI
from fastapi import APIRouter, Depends, HTTPException

# importa leitura de token bearer
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

# importa models de métricas
from app.models.metrics import MetricasCreate
from app.models.metrics import MetricasResponse

# importa funções do service de métricas
from app.services.metrics_service import buscar_historico
from app.services.metrics_service import buscar_metricas
from app.services.metrics_service import salvar_metricas

# importa função que valida token JWT
from app.services.security import verificar_token


# cria roteador de métricas
roteador_metricas = APIRouter()

# exige token bearer no header
security = HTTPBearer()


# função que valida usuário antes de abrir rota protegida
def validar_usuario(
    credenciais: HTTPAuthorizationCredentials = Depends(security)
):
    # pega somente token puro
    token = credenciais.credentials

    try:
        # valida token
        dados = verificar_token(token)

        return dados

    except:
        # se token inválido bloqueia acesso
        raise HTTPException(
            status_code=401,
            detail="Token inválido"
        )


# rota protegida - busca última métrica
@roteador_metricas.get("/metrics", response_model=MetricasResponse)
async def metrics(usuario=Depends(validar_usuario)):
    # busca último registro
    dados = buscar_metricas()

    return dados


# rota para salvar novas métricas
@roteador_metricas.post("/metrics")
async def criar_metricas(dados: MetricasCreate):
    # salva dados no banco
    resultado = salvar_metricas(dados)

    return resultado


# rota histórico de métricas
@roteador_metricas.get(
    "/metrics/historico",
    response_model=List[MetricasResponse]
)
async def historico(limit: int = 10):
    # busca histórico limitado
    return buscar_historico(limit)
