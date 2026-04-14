# importa a base para criar modelos Pydantic
from pydantic import BaseModel


class Engajamento(BaseModel):                          # define o bloco de engajamento
    curtidas: int                                      # total de curtidas
    comentarios: int                                   # total de comentários
    salvamentos: int                                   # total de salvamentos


# define o modelo de resposta das métricas
class MetricasResponse(BaseModel):
    seguidores: int                                    # total de seguidores
    alcance: int                                       # total de alcance
    impressoes: int                                    # total de impressões
    # bloco interno de engajamento
    engajamento: Engajamento


# define o modelo de entrada para criar métricas
class MetricasCreate(BaseModel):
                                                       # seguidores recebidos na requisição
    seguidores: int
    alcance: int                                       # alcance recebido na requisição
    # impressões recebidas na requisição
    impressoes: int
    # curtidas recebidas na requisição
    curtidas: int
    # comentários recebidos na requisição
    comentarios: int
    # salvamentos recebidos na requisição
    salvamentos: int
