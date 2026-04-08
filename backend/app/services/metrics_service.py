def buscar_metricas():                             # define uma função que retorna os dados de métricas
    return {
        "seguidores": 1250,                        # número simulado de seguidores
        "alcance": 8400,                           # número simulado de alcance
        "impressoes": 13200,                       # número simulado de impressões
        "engajamento": {                           # objeto interno com dados de engajamento
            "curtidas": 320,                       # número simulado de curtidas
            "comentarios": 48,                     # número simulado de comentários
            "salvamentos": 27                      # número simulado de salvamentos
        }
    }