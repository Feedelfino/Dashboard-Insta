from fastapi import APIRouter                            # importa a classe usada para agrupar rotas
from app.services.metrics_service import buscar_metricas # importa a função de service que devolve as métricas

roteador_metricas = APIRouter()                         # cria um roteador específico para rotas de métricas


@roteador_metricas.get("/metrics")                      # cria a rota GET /metrics
async def metrics():                                    # função executada quando alguém acessa /metrics
    dados = buscar_metricas()                           # chama o service para obter os dados
    return dados                                        # devolve os dados como resposta da API