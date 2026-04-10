from fastapi import APIRouter                             # importa a classe usada para agrupar rotas
from app.services.metrics_service import buscar_metricas  # importa a função de busca
from app.services.metrics_service import salvar_metricas  # importa a função de salvar
from app.models.metrics import MetricasResponse          # importa o model da resposta
from app.models.metrics import MetricasCreate            # importa o model de entrada

roteador_metricas = APIRouter()                          # cria o roteador de métricas


@roteador_metricas.get("/metrics", response_model=MetricasResponse)   # cria a rota GET /metrics
async def metrics():                                     # função executada ao acessar /metrics
    dados = buscar_metricas()                            # chama o service para buscar os dados
    return dados                                         # devolve os dados como resposta


@roteador_metricas.post("/metrics")                      # cria a rota POST /metrics
async def criar_metricas(dados: MetricasCreate):         # recebe os dados enviados no corpo da requisição
    resultado = salvar_metricas(dados)                   # chama o service para salvar os dados no banco
    return resultado                                     # devolve a resposta de confirmação