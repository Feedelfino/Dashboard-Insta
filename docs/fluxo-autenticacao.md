# Fluxo de Autenticação — Dashboard Insta Analytics

## Objetivo

Este documento explica o fluxo de autenticação usado no projeto Dashboard Insta Analytics.

A autenticação permite que apenas usuários válidos acessem áreas protegidas da aplicação, como o dashboard de métricas.

## Visão Geral do Fluxo

1. Usuário acessa a tela de login.
2. Usuário informa email e senha.
3. Frontend envia os dados para o backend.
4. Backend valida as credenciais.
5. Backend gera um token JWT.
6. Frontend salva o token no navegador.
7. Usuário é redirecionado para o dashboard.
8. Dashboard usa o token para acessar rotas protegidas.

## Fluxo Passo a Passo

### 1. Tela de Login

Arquivo principal:

- frontend/src/pages/LoginPage.tsx

A tela de login captura dois dados:

- email
- senha

Esses valores são controlados com useState.

### 2. Envio para o Backend

Quando o usuário clica no botão Entrar, o frontend executa a função handleLogin.

Essa função faz uma requisição HTTP para o backend usando fetch.

Endpoint utilizado:

- POST /auth/login

Dados enviados:

- email
- senha

### 3. Validação no Backend

O backend recebe a requisição e verifica:

- se o usuário existe no banco
- se a senha informada corresponde à senha cadastrada
- se os dados são válidos

Se as credenciais estiverem corretas, o backend gera um token JWT.

### 4. Retorno do Token

Após login bem-sucedido, o backend retorna um JSON com o token.

Exemplo conceitual de retorno:

- access_token
- token_type

O token é usado para provar que o usuário está autenticado.

### 5. Armazenamento no Frontend

O frontend salva o token no navegador usando localStorage.

Isso permite que o sistema mantenha o usuário autenticado enquanto o token existir no navegador.

### 6. Redirecionamento

Após salvar o token, o frontend redireciona o usuário para:

- /dashboard

### 7. Proteção da Rota Dashboard

Arquivo principal:

- frontend/src/pages/DashboardPage.tsx

Antes de exibir o dashboard, a página verifica se existe token salvo no localStorage.

Se não existir token, o usuário é redirecionado para a tela de login.

### 8. Acesso a Rotas Protegidas

Para acessar rotas protegidas, o frontend envia o token no cabeçalho Authorization.

Formato usado:

- Authorization: Bearer token

Rotas protegidas utilizadas atualmente:

- GET /metrics
- GET /metrics/historico

## Resumo do Fluxo

Usuário faz login  
↓  
Frontend envia email e senha  
↓  
Backend valida usuário  
↓  
Backend retorna JWT  
↓  
Frontend salva token  
↓  
Frontend acessa dashboard  
↓  
Dashboard envia token nas requisições  
↓  
Backend valida token  
↓  
Dados protegidos são retornados  

## Possíveis Melhorias Futuras

- criar botão de logout
- remover token ao sair
- validar expiração do token
- proteger rotas usando componente específico
- melhorar mensagens de erro no login
- tratar token inválido ou expirado
- trocar localStorage por estratégia mais segura em produção

## Aprendizado Principal

O fluxo de autenticação mostra como frontend e backend trabalham juntos para controlar acesso a áreas privadas do sistema.

Esse fluxo é comum em sistemas reais, como CRMs, dashboards administrativos, ERPs, plataformas SaaS e aplicações internas.