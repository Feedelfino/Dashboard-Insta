# Changelog — Dashboard Insta Analytics

---

# Etapa 13 — Refatoração de UI/UX

## Dashboard

- Criação de container centralizado
- Adição de header institucional
- Organização visual dos cards
- Hierarquia visual para métricas
- Implementação de gráfico responsivo
- Formatação de datas no gráfico
- Melhoria visual do loading

## LoginPage

- Refatoração estrutural da tela
- Criação de painel visual estilo SaaS
- Inclusão de elemento visual simulando analytics
- Melhor organização do formulário
- Estrutura dividida em duas colunas

## Conceitos praticados

- React
- TypeScript
- Flexbox
- Responsividade
- Hierarquia visual
- Debug de JSX
- Estruturação de layout

---

# Refatoração de Arquitetura Frontend

## Serviços e API

- Criação da pasta `services`
- Criação do arquivo `api.ts`
- Centralização da URL base da API
- Criação de função centralizada para headers HTTP
- Centralização do gerenciamento de token JWT
- Refatoração da autenticação para camada de serviço
- Redução de acoplamento entre páginas e backend

## LoginPage

- Refatoração da lógica de login
- Remoção de `fetch` direto da página
- Integração da tela com função `login()` do `api.ts`

## DashboardPage

- Refatoração parcial das chamadas de API
- Centralização dos headers de autenticação
- Preparação estrutural para desacoplamento completo da página

## Conceitos praticados

- Separação de responsabilidades
- Arquitetura frontend
- Camada de serviços
- Reutilização de código
- Redução de duplicação
- Organização de infraestrutura frontend