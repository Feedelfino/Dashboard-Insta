from app.database import conectar_db                   # importa a função de conexão com o banco


def criar_tabela():                                    # função que cria a tabela metrics
    conn = conectar_db()                               # abre conexão com o banco
    cursor = conn.cursor()                             # cria cursor para executar SQL

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS metrics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        seguidores INTEGER,
        alcance INTEGER,
        impressoes INTEGER,
        curtidas INTEGER,
        comentarios INTEGER,
        salvamentos INTEGER,
        criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()                                      # salva a criação da tabela
    conn.close()                                       # fecha conexão


def inserir_dados_iniciais():                          # função que insere um registro inicial no banco
    conn = conectar_db()                               # abre conexão com o banco
    cursor = conn.cursor()                             # cria cursor para executar SQL

    cursor.execute("""
    INSERT INTO metrics (
        seguidores, alcance, impressoes,
        curtidas, comentarios, salvamentos
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """, (1250, 8400, 13200, 320, 48, 27))            # insere valores iniciais

    conn.commit()                                      # salva os dados inseridos
    conn.close()                                       # fecha conexão


if __name__ == "__main__":                             # executa quando rodar o arquivo como módulo
    criar_tabela()                                     # cria a tabela
    inserir_dados_iniciais()                           # insere os dados iniciais
    
    
def criar_tabela_usuarios():                         # função que cria a tabela de usuários
    conn = conectar_db()                             # abre conexão com o banco
    cursor = conn.cursor()                           # cria cursor para executar SQL

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        senha_hash TEXT NOT NULL,
        criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()                                    # salva criação da tabela
    conn.close()                                     # fecha conexão

if __name__ == "__main__":                           # executa quando rodar o arquivo como módulo
    criar_tabela()                                   # cria a tabela metrics
    criar_tabela_usuarios()                          # cria a tabela users
    inserir_dados_iniciais()                         # insere os dados iniciais de metrics