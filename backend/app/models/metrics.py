from pydantic import BaseModel                         # importa a classe base usada para criar modelos de dados


class Engajamento(BaseModel):                          # define o modelo do bloco de engajamento
    curtidas: int                                      # quantidade de curtidas
    comentarios: int                                   # quantidade de comentários
    salvamentos: int                                   # quantidade de salvamentos


class MetricasResponse(BaseModel):                    # define o modelo completo da resposta de métricas
    seguidores: int                                    # total de seguidores
    alcance: int                                       # total de alcance
    impressoes: int                                    # total de impressões
    engajamento: Engajamento                           # bloco interno de engajamento
    
class MetricasCreate(BaseModel):                    # define o modelo de entrada para criar métricas
    seguidores: int                                 # total de seguidores recebido na requisição
    alcance: int                                    # total de alcance recebido na requisição
    impressoes: int                                 # total de impressões recebido na requisição
    curtidas: int                                   # total de curtidas recebido na requisição
    comentarios: int                                # total de comentários recebido na requisição
    salvamentos: int                                # total de salvamentos recebido na requisição