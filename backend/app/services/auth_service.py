# importa biblioteca de hash
import bcrypt
# importa função de conexão com o banco
from app.database import conectar_db
# importa model de cadastro
from app.models.auth import UserCreate
from app.models.auth import UserLogin                  # importa model de login
# importa função para gerar JWT
from app.services.security import criar_token


# função que transforma senha em hash
def gerar_hash_senha(senha: str) -> str:
    # converte texto para bytes
    senha_bytes = senha.encode("utf-8")
    salt = bcrypt.gensalt()                            # gera salt de segurança
    senha_hash = bcrypt.hashpw(senha_bytes, salt)      # cria hash da senha
    # retorna hash como texto
    return senha_hash.decode("utf-8")


# compara senha digitada com hash salvo
def verificar_senha(senha: str, senha_hash: str) -> bool:
    return bcrypt.checkpw(
        # converte senha digitada para bytes
        senha.encode("utf-8"),
        # converte hash salvo para bytes
        senha_hash.encode("utf-8")
    )


# função que registra usuário no banco
def registrar_usuario(dados: UserCreate):
    conn = conectar_db()                               # abre conexão com o banco
    # cria cursor para executar SQL
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id FROM users WHERE email = ?",
        (dados.email,)
    )                                                  # verifica se já existe usuário com esse email

    usuario_existente = cursor.fetchone()              # pega resultado da consulta

    if usuario_existente:                              # se já existir usuário com esse email
        conn.close()                                   # fecha conexão
        return {"erro": "Email já cadastrado"}         # retorna erro simples

    # gera hash da senha antes de salvar
    senha_hash = gerar_hash_senha(dados.senha)

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

    # resposta de sucesso
    return {"mensagem": "Usuário cadastrado com sucesso"}


# função que autentica usuário
def autenticar_usuario(dados: UserLogin):
    conn = conectar_db()                               # abre conexão com o banco
    # cria cursor para executar SQL
    cursor = conn.cursor()

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

    # gera token do usuário autenticado
    token = criar_token({
        "sub": usuario["email"],
        "id": usuario["id"]
    })

    # retorna token de acesso
    return {
        "access_token": token,
        "token_type": "bearer"
    }
