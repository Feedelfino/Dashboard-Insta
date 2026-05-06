# Dashboard Insta Analytics

Projeto full stack desenvolvido para estudo prático de desenvolvimento web, integração entre frontend e backend, autenticação JWT e visualização de métricas em dashboard.

## Objetivo

Criar uma aplicação de analytics inspirada em métricas do Instagram, com autenticação, rotas protegidas, consumo de API e exibição visual de dados.

## Status do Projeto

Em desenvolvimento.

Funcionalidades já implementadas:

- Backend com FastAPI
- Banco SQLite
- Autenticação com JWT
- Login integrado ao frontend
- Proteção de rotas
- Dashboard com cards de métricas
- Gráfico com histórico de seguidores usando Recharts

## Tecnologias

### Backend

- Python
- FastAPI
- SQLite
- JWT
- Uvicorn

### Frontend

- React
- TypeScript
- Vite
- React Router DOM
- Recharts

### Versionamento

- Git
- GitHub

## Como rodar o projeto

### Backend

```bash
cd backend
python -m pip install -r requirements.txt
uvicorn app.main:app --reload