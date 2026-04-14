from fastapi import FastAPI                            # importa o framework FastAPI
from fastapi.middleware.cors import CORSMiddleware    # importa o middleware de CORS
from app.config import configuracoes                  # importa as configurações do projeto
from app.routes.metrics import roteador_metricas      # importa o roteador de métricas
from app.routes.auth import roteador_auth              # importa o roteador de autenticação

app = FastAPI(                                        # cria a aplicação principal
    title="Instagram Analytics API",                  # nome da API
    description="API para análise de métricas",       # descrição da API
    version="1.0.0"                                   # versão da API
)

app.add_middleware(                                   # adiciona middleware à aplicação
    CORSMiddleware,                                   # middleware de CORS
    allow_origins=[configuracoes.frontend_url],       # libera o frontend configurado
    allow_credentials=True,                           # permite credenciais
    allow_methods=["*"],                              # permite todos os métodos
    allow_headers=["*"],                              # permite todos os headers
)

app.include_router(roteador_metricas)                 # registra as rotas de métricas
app.include_router(roteador_auth)                      # registra rotas de autenticação

@app.get("/")                                         # rota GET na raiz
async def raiz():                                     # função executada ao acessar /
    return {
        "status": "online",                           # status da API
        "mensagem": "Backend funcionando"             # mensagem de confirmação
    }

@app.get("/health")                                   # rota GET em /health
async def health():                                   # função executada ao acessar /health
    return {
        "ok": True                                    # indica que a aplicação está saudável
    }

@app.get("/teste")                                    # rota GET em /teste
async def rota_teste():                               # função executada ao acessar /teste
    return {
        "mensagem": "Rota teste funcionando"          # resposta de teste
    }

@app.get("/config-teste")                             # rota GET em /config-teste
async def config_teste():                             # função executada ao acessar /config-teste
    return {
        "frontend_url": configuracoes.frontend_url,   # mostra a URL do frontend lida do config
        "redirect_uri": configuracoes.redirect_uri    # mostra a URI lida do config
    }