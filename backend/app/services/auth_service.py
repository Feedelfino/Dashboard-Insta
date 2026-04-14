import bcrypt                                          # importa biblioteca de hash
from app.database import conectar_db                   # importa função de conexão com o banco
from app.models.auth import UserCreate                 # importa model de cadastro
from app.models.auth import UserLogin                  # importa model de login


def gerar_hash_senha(senha: str) -> str:               # função que transforma senha em hash
    senha_bytes = senha.encode("utf-8")                # converte texto para bytes
    salt = bcrypt.gensalt()                            # gera salt de segurança
    senha_hash = bcrypt.hashpw(senha_bytes, salt)      # cria hash da senha
    return senha_hash.decode("utf-8")                  # retorna hash como texto


def verificar_senha(senha: str, senha_hash: str) -> bool:   # compara senha digitada com hash salvo
    return bcrypt.checkpw(
        senha.encode("utf-8"),                         # converte senha digitada para bytes
        senha_hash.encode("utf-8")                     # converte hash salvo para bytes
    )


def registrar_usuario(dados: UserCreate):              # função que registra usuário no banco
    conn = conectar_db()                               # abre conexão com o banco
    cursor = conn.cursor()                             # cria cursor para executar SQL

    cursor.execute(
        "SELECT id FROM users WHERE email = ?",
        (dados.email,)
    )                                                  # verifica se já existe usuário com esse email

    usuario_existente = cursor.fetchone()              # pega resultado da consulta

    if usuario_existente:                              # se já existir usuário com esse email
        conn.close()                                   # fecha conexão
        return {"erro": "Email já cadastrado"}         # retorna erro simples

    senha_hash = gerar_hash_senha(dados.senha)         # gera hash da senha antes de salvar

    cursor.execute("""
    INSERT INTO users (nome, email, senha_hash)
    VALUES (?, ?, ?)
    """, (
        dados.nome,
        dados.email,
        senha_hash
    ))                                                 # insere usuário no banco

    conn.commit()                                      # salva inserção
    conn.close()                                       # fecha conexão

    return {"mensagem": "Usuário cadastrado com sucesso"}   # resposta de sucesso


def autenticar_usuario(dados: UserLogin):              # função que autentica usuário
    conn = conectar_db()                               # abre conexão com o banco
    cursor = conn.cursor()                             # cria cursor para executar SQL

    cursor.execute(
        "SELECT id, nome, email, senha_hash FROM users WHERE email = ?",
        (dados.email,)
    )                                                  # busca usuário pelo email

    usuario = cursor.fetchone()                        # pega resultado
    conn.close()                                       # fecha conexão

    if usuario is None:                                # se não encontrou usuário
        return {"erro": "Usuário não encontrado"}

    senha_valida = verificar_senha(
        dados.senha,
        usuario["senha_hash"]
    )                                                  # compara senha digitada com hash salvo

    if not senha_valida:                               # se senha estiver errada
        return {"erro": "Senha inválida"}

    return {                                           # resposta básica de sucesso
        "mensagem": "Login realizado com sucesso",
        "usuario": {
            "id": usuario["id"],
            "nome": usuario["nome"],
            "email": usuario["email"]
        }
    }