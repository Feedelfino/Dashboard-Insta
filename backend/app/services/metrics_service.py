from app.database import conectar_db                 # importa a função de conexão com o banco
from app.models.metrics import MetricasResponse      # importa o model principal da resposta
from app.models.metrics import Engajamento           # importa o model interno de engajamento
from app.models.metrics import MetricasCreate        # importa o model de entrada para criação


def buscar_metricas():                               # define a função que busca métricas no banco
    conn = conectar_db()                             # abre conexão com o banco
    cursor = conn.cursor()                           # cria cursor para executar SQL

    cursor.execute("""
    SELECT seguidores, alcance, impressoes, curtidas, comentarios, salvamentos
    FROM metrics
    ORDER BY id DESC
    LIMIT 1
    """)

    registro = cursor.fetchone()                     # pega uma única linha do resultado
    conn.close()                                     # fecha a conexão com o banco

    if registro is None:                             # verifica se não existe dado salvo
        return MetricasResponse(                     # retorna uma resposta vazia padronizada
            seguidores=0,
            alcance=0,
            impressoes=0,
            engajamento=Engajamento(
                curtidas=0,
                comentarios=0,
                salvamentos=0
            )
        )

    return MetricasResponse(                         # monta e retorna a resposta usando os dados do banco
        seguidores=registro["seguidores"],           # pega seguidores da linha retornada
        alcance=registro["alcance"],                 # pega alcance da linha retornada
        impressoes=registro["impressoes"],           # pega impressões da linha retornada
        engajamento=Engajamento(                     # monta o bloco de engajamento
            curtidas=registro["curtidas"],           # pega curtidas da linha retornada
            comentarios=registro["comentarios"],     # pega comentários da linha retornada
            salvamentos=registro["salvamentos"]      # pega salvamentos da linha retornada
        )
    )


def salvar_metricas(dados: MetricasCreate):          # define função que salva métricas no banco
    conn = conectar_db()                             # abre conexão com o banco
    cursor = conn.cursor()                           # cria cursor para executar SQL

    cursor.execute("""
    INSERT INTO metrics (
        seguidores, alcance, impressoes,
        curtidas, comentarios, salvamentos
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        dados.seguidores,                            # usa o valor de seguidores recebido
        dados.alcance,                               # usa o valor de alcance recebido
        dados.impressoes,                            # usa o valor de impressões recebido
        dados.curtidas,                              # usa o valor de curtidas recebido
        dados.comentarios,                           # usa o valor de comentários recebido
        dados.salvamentos                            # usa o valor de salvamentos recebido
    ))

    conn.commit()                                    # salva a inserção no banco
    conn.close()                                     # fecha conexão

    return {                                         # devolve confirmação
        "mensagem": "Métricas salvas com sucesso"
    }