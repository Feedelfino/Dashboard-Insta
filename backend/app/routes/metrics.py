# importa tipagem para listas
from typing import List
# importa a classe usada para agrupar rotas
from fastapi import APIRouter

from app.models.metrics import MetricasCreate          # importa o model de entrada
# importa o model de resposta
from app.models.metrics import MetricasResponse
# importa a função de histórico
from app.services.metrics_service import buscar_historico
# importa a função de busca da métrica atual
from app.services.metrics_service import buscar_metricas
# importa a função de salvar métricas
from app.services.metrics_service import salvar_metricas

# cria o roteador de métricas
roteador_metricas = APIRouter()


# cria a rota GET /metrics
@roteador_metricas.get("/metrics", response_model=MetricasResponse)
async def metrics():                                   # função executada ao acessar /metrics
    # chama o service para buscar o último registro
    dados = buscar_metricas()
    return dados                                       # devolve os dados como resposta


# cria a rota POST /metrics
@roteador_metricas.post("/metrics")
# recebe dados enviados no corpo da requisição
async def criar_metricas(dados: MetricasCreate):
    # chama o service para salvar os dados no banco
    resultado = salvar_metricas(dados)
    # devolve resposta de confirmação
    return resultado


@roteador_metricas.get(
    "/metrics/historico",
    response_model=List[MetricasResponse]
)                                                      # cria a rota GET /metrics/historico
# recebe um limite opcional via query param
async def historico(limit: int = 10):
    # chama o service para buscar o histórico
    return buscar_historico(limit)
