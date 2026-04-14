from pydantic import BaseModel                         # importa a base para criar modelos Pydantic


class Engajamento(BaseModel):                          # define o bloco de engajamento
    curtidas: int                                      # total de curtidas
    comentarios: int                                   # total de comentários
    salvamentos: int                                   # total de salvamentos


class MetricasResponse(BaseModel):                     # define o modelo de resposta das métricas
    seguidores: int                                    # total de seguidores
    alcance: int                                       # total de alcance
    impressoes: int                                    # total de impressões
    criado_em: str                                     # data/hora em que o registro foi criado
    engajamento: Engajamento                           # bloco interno de engajamento


class MetricasCreate(BaseModel):                       # define o modelo de entrada para criar métricas
    seguidores: int                                    # seguidores recebidos na requisição
    alcance: int                                       # alcance recebido na requisição
    impressoes: int                                    # impressões recebidas na requisição
    curtidas: int                                      # curtidas recebidas na requisição
    comentarios: int                                   # comentários recebidos na requisição
    salvamentos: int                                   # salvamentos recebidos na requisição