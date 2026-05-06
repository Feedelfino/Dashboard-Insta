# Roadmap — Dashboard Insta Analytics

## Objetivo

Este documento organiza a evolução do projeto Dashboard Insta Analytics, separando o que já foi implementado, o que está em andamento e quais serão os próximos passos.

## Status Geral

O projeto está em desenvolvimento.

A base full stack já está funcional, com backend, autenticação, frontend integrado, dashboard protegido e visualização inicial de métricas.

## Concluído

### Backend

- Estrutura inicial com FastAPI
- Organização em camadas
- Banco SQLite configurado
- Endpoints de métricas
- Endpoint de histórico de métricas
- Cadastro de usuários
- Login de usuários
- Hash de senha com bcrypt
- Geração de token JWT
- Validação de Bearer Token
- Rotas protegidas
- Documentação automática com Swagger

### Frontend

- Projeto React com TypeScript e Vite
- Tela de login
- Captura de email e senha com useState
- Integração do login com backend
- Armazenamento do JWT no localStorage
- React Router configurado
- Rota de dashboard
- Proteção da rota dashboard
- Consumo do endpoint /metrics
- Consumo do endpoint /metrics/historico
- Cards de métricas
- Gráfico de evolução de seguidores com Recharts

### Documentação

- README inicial
- Proposta do projeto
- Documento de arquitetura
- Fluxo de autenticação
- Fluxo do dashboard

### Versionamento

- Repositório GitHub configurado
- Commits de evolução
- Branch feature/ui-dashboard criada

## Em Andamento

### UI/UX do Dashboard

Melhorar a experiência visual da tela de dashboard.

Pontos previstos:

- melhorar espaçamento geral
- melhorar hierarquia visual
- formatar datas do gráfico
- melhorar visual dos cards
- organizar layout para parecer mais próximo de um produto real

## Próximas Etapas

### 1. Melhorar UI/UX

Prioridade: alta

Objetivo:

- deixar o dashboard mais profissional
- melhorar leitura das métricas
- preparar a tela para portfólio

### 2. Criar Logout

Prioridade: alta

Objetivo:

- permitir que o usuário saia do sistema
- remover token do localStorage
- redirecionar para login

### 3. Formatar Datas

Prioridade: média

Objetivo:

- transformar datas técnicas em formato amigável
- melhorar leitura do gráfico

### 4. Melhorar Tratamento de Erros

Prioridade: média

Objetivo:

- mostrar mensagens mais claras ao usuário
- diferenciar erro de login, erro de conexão e erro de token

### 5. Separar Serviços de API

Prioridade: média

Objetivo:

- criar uma camada services/api.ts no frontend
- evitar repetição de fetch
- melhorar organização do código

### 6. Responsividade

Prioridade: média

Objetivo:

- adaptar dashboard para telas menores
- melhorar experiência em dispositivos móveis

### 7. Deploy

Prioridade: alta

Objetivo:

- colocar backend e frontend online
- tornar o projeto acessível para portfólio

### 8. Integração com API Real

Prioridade: futura

Objetivo:

- conectar com dados reais de redes sociais
- evoluir o projeto para uma aplicação mais próxima do mercado

## Melhorias Futuras

- filtros por período
- gráficos de alcance e impressões
- cards de engajamento
- múltiplas contas
- perfil do usuário
- dashboard administrativo
- exportação de relatório
- testes automatizados
- documentação de endpoints
- deploy com variáveis de ambiente

## Critério de Versão Mínima para Portfólio

Para considerar o projeto apresentável no portfólio, ele deve ter:

- login funcionando
- dashboard protegido
- cards com métricas
- gráfico funcional
- README organizado
- documentação básica
- deploy online
- prints ou demonstração visual
- instruções claras de execução

## Observações

O roadmap pode mudar conforme o projeto evoluir.

O objetivo principal neste momento é consolidar uma base full stack funcional, bem documentada e apresentável como projeto de portfólio.