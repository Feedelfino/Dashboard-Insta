import sqlite3                                 # importa o SQLite (banco leve embutido no Python)


def conectar_db():                             # função que cria conexão com o banco
    conexao = sqlite3.connect("database.db")   # cria (ou abre) o arquivo do banco
    conexao.row_factory = sqlite3.Row          # permite acessar colunas por nome
    return conexao                             # retorna a conexão