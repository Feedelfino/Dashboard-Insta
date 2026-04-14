# importa a função de conexão com o banco
from app.database import conectar_db
# importa o model principal da resposta
from app.models.metrics import MetricasResponse
# importa o model interno de engajamento
from app.models.metrics import Engajamento
# importa o model de entrada para criação
from app.models.metrics import MetricasCreate


def buscar_metricas():                                 # define a função que busca a métrica mais recente
    conn = conectar_db()                               # abre conexão com o banco
    # cria cursor para executar SQL
    cursor = conn.cursor()

    cursor.execute("""
    SELECT seguidores, alcance, impressoes, curtidas, comentarios, salvamentos
    FROM metrics
    ORDER BY id DESC
    LIMIT 1
    """)                                               # busca o registro mais recente

    # pega uma única linha do resultado
    registro = cursor.fetchone()
    conn.close()                                       # fecha conexão com o banco

    if registro is None:                               # verifica se não há registros
        return MetricasResponse(                       # retorna resposta vazia padronizada
            seguidores=0,
            alcance=0,
            impressoes=0,
            engajamento=Engajamento(
                curtidas=0,
                comentarios=0,
                salvamentos=0
            )
        )

    return MetricasResponse(                           # monta a resposta com o registro encontrado
        seguidores=registro["seguidores"],
        alcance=registro["alcance"],
        impressoes=registro["impressoes"],
        engajamento=Engajamento(
            curtidas=registro["curtidas"],
            comentarios=registro["comentarios"],
            salvamentos=registro["salvamentos"]
        )
    )


# define função que salva métricas no banco
def salvar_metricas(dados: MetricasCreate):
    conn = conectar_db()                              # abre conexão com o banco
    cursor = conn.cursor()                            # cria cursor para executar SQL

    cursor.execute("""
    INSERT INTO metrics (
        seguidores, alcance, impressoes,
        curtidas, comentarios, salvamentos
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        dados.seguidores,
        dados.alcance,
        dados.impressoes,
        dados.curtidas,
        dados.comentarios,
        dados.salvamentos
    ))                                                # insere os dados recebidos

    conn.commit()                                     # salva inserção
    conn.close()                                      # fecha conexão

    return {
        "mensagem": "Métricas salvas com sucesso"
    }                                                 # devolve confirmação simples


# define função que busca o histórico de métricas
def buscar_historico(limit: int = 10):
    conn = conectar_db()                              # abre conexão com o banco
    cursor = conn.cursor()                            # cria cursor para executar SQL

    cursor.execute("""
    SELECT seguidores, alcance, impressoes, curtidas, comentarios, salvamentos
    FROM metrics
    ORDER BY id DESC
    LIMIT ?
    """, (limit,))                                    # busca os últimos registros limitados pelo parâmetro

    registros = cursor.fetchall()                     # pega várias linhas
    conn.close()                                      # fecha conexão

    # lista que vai armazenar os resultados
    resultado = []

    for registro in registros:                        # percorre cada linha retornada
        resultado.append(
            MetricasResponse(
                seguidores=registro["seguidores"],
                alcance=registro["alcance"],
                impressoes=registro["impressoes"],
                engajamento=Engajamento(
                    curtidas=registro["curtidas"],
                    comentarios=registro["comentarios"],
                    salvamentos=registro["salvamentos"]
                )
            )
        )

    return resultado                                  # devolve a lista de métricas
