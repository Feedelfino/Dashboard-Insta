from dotenv import load_dotenv                 # importa função que carrega o arquivo .env
from pydantic_settings import BaseSettings    # classe que permite criar configurações baseadas em variáveis de ambiente

load_dotenv()                                 # lê o arquivo .env e coloca as variáveis no ambiente do sistema

class Configuracoes(BaseSettings):             # cria uma classe que representa todas as configurações do projeto
    instagram_app_id: str                      # espera uma variável chamada INSTAGRAM_APP_ID (tipo string)
    instagram_app_secret: str                  # espera INSTAGRAM_APP_SECRET (tipo string)
    redirect_uri: str = "http://localhost:8000/auth/callback"   # valor padrão se não vier do .env
    frontend_url: str = "http://localhost:5173"                 # valor padrão do frontend

configuracoes = Configuracoes()               # cria uma instância única que será usada no projeto inteiro