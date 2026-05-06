# Arquitetura do Projeto — Dashboard Insta Analytics

## Visão Geral

O Dashboard Insta Analytics é uma aplicação full stack composta por duas partes principais:

- Backend: responsável pela API, autenticação, regras de negócio e banco de dados.
- Frontend: responsável pela interface, navegação, login do usuário e exibição das métricas.

A comunicação entre frontend e backend acontece por meio de requisições HTTP para endpoints da API.

## Estrutura Geral

Dashboard-Insta/

- backend/
  - app/
    - models/
    - routes/
    - services/
    - config.py
    - database.py
    - init_db.py
    - main.py
  - database.db
  - requirements.txt
  - .env

- frontend/
  - src/
    - pages/
      - LoginPage.tsx
      - DashboardPage.tsx
    - App.tsx
    - main.tsx
    - index.css
  - package.json
  - vite.config.ts

- docs/

## Backend

O backend foi desenvolvido com FastAPI e segue uma organização em camadas.

### main.py

Arquivo principal da API.

Responsável por:

- criar a aplicação FastAPI
- registrar as rotas
- configurar recursos globais da API

### routes/

Camada responsável pelos endpoints da aplicação.

Exemplos:

- rotas de autenticação
- rotas de métricas
- rotas de teste/saúde da API

Essa camada recebe requisições HTTP e direciona para a lógica adequada.

### services/

Camada responsável pela lógica de negócio.

Exemplos:

- validação de senha
- geração e verificação de token JWT
- regras relacionadas à autenticação

### models/

Camada responsável pelos modelos de dados usados pela aplicação.

Ela ajuda a estruturar os dados esperados nas requisições e respostas.

### database.py

Arquivo responsável pela conexão com o banco SQLite.

### database.db

Arquivo físico do banco de dados SQLite.

### .env

Arquivo usado para armazenar variáveis de ambiente, como configurações sensíveis.

## Frontend

O frontend foi desenvolvido com React, TypeScript e Vite.

### main.tsx

Ponto de entrada da aplicação React.

Responsável por inicializar o React e habilitar o sistema de rotas com BrowserRouter.

### App.tsx

Central de rotas do frontend.

Responsável por definir quais páginas serão exibidas em cada caminho da aplicação.

Exemplo:

- / → LoginPage
- /dashboard → DashboardPage

### pages/LoginPage.tsx

Tela responsável pelo login do usuário.

Responsabilidades:

- capturar email e senha
- enviar credenciais para o backend
- receber token JWT
- salvar token no localStorage
- redirecionar usuário para o dashboard

### pages/DashboardPage.tsx

Tela principal protegida.

Responsabilidades:

- verificar se existe token salvo
- redirecionar usuário não autenticado para login
- consumir endpoint /metrics
- consumir endpoint /metrics/historico
- exibir cards com métricas
- exibir gráfico com histórico

## Comunicação entre Frontend e Backend

O frontend se comunica com o backend usando fetch.

Fluxo geral:

1. Frontend faz uma requisição para um endpoint FastAPI.
2. Backend valida a requisição.
3. Backend consulta o banco ou executa uma regra de negócio.
4. Backend retorna JSON.
5. Frontend renderiza os dados na tela.

## Autenticação

A autenticação usa JWT.

Fluxo geral:

1. Usuário envia email e senha.
2. Backend valida credenciais.
3. Backend gera JWT.
4. Frontend salva token no localStorage.
5. Frontend envia token em rotas protegidas.
6. Backend valida Bearer Token.

## Decisões Técnicas

### FastAPI

Escolhido pela facilidade de criação de APIs, boa documentação automática e integração simples com Python.

### SQLite

Escolhido por ser leve, local e adequado para fase inicial de aprendizado e prototipação.

### React + TypeScript

Escolhidos para construir uma interface moderna, componentizada e com maior segurança de tipos.

### Recharts

Usado para criar visualizações gráficas a partir do histórico de métricas.

## Estado Atual da Arquitetura

A arquitetura atual já permite:

- autenticação funcional
- rotas protegidas
- frontend consumindo backend
- dashboard com dados reais
- visualização gráfica

Ainda há espaço para melhorias como:

- separação de componentes visuais
- criação de camada services/api.ts no frontend
- tratamento mais robusto de erros
- deploy separado de frontend e backend
- integração com API real do Instagram