# Aprendizados — Dashboard Insta Analytics

## Objetivo

Este documento registra os principais aprendizados adquiridos durante o desenvolvimento do projeto Dashboard Insta Analytics.

O foco é documentar não apenas o que foi construído, mas também os conceitos, erros, decisões e soluções encontradas ao longo do processo.

## Aprendizados de Backend

### FastAPI

Foi praticada a criação de uma API usando FastAPI, com rotas organizadas e documentação automática pelo Swagger.

Aprendizados principais:

- criação de endpoints
- organização de rotas
- uso do Uvicorn para rodar a API
- leitura de erros no terminal
- validação de requisições

### Banco de Dados SQLite

O projeto usa SQLite como banco local.

Aprendizados principais:

- uso de banco baseado em arquivo
- consulta de tabelas com Python
- verificação de usuários cadastrados
- entendimento de estrutura básica de persistência

### Autenticação JWT

Foi implementado login com geração e validação de token JWT.

Aprendizados principais:

- diferença entre login e autenticação contínua
- uso de Bearer Token
- proteção de rotas
- validação de usuário antes de liberar dados protegidos

### Senhas com Hash

O projeto utiliza bcrypt para lidar com senhas.

Aprendizados principais:

- senha não deve ser salva em texto puro
- hash protege credenciais
- login compara senha digitada com hash armazenado

## Aprendizados de Frontend

### React

Foi praticada a criação de telas com React.

Aprendizados principais:

- criação de componentes
- separação de páginas
- uso de JSX
- renderização condicional
- atualização da interface com base no estado

### TypeScript

O projeto usa TypeScript para aumentar segurança no código.

Aprendizados principais:

- criação de tipos
- diferença entre objeto único e lista
- uso de Metric e Metric[]
- evitar uso desnecessário de any
- leitura de erros de tipagem

### useState

Foi usado para guardar informações dinâmicas na tela.

Exemplos:

- email
- senha
- métrica atual
- histórico de métricas
- loading

### useEffect

Foi usado para executar ações quando a tela carrega.

Aprendizados principais:

- buscar dados automaticamente
- chamar APIs ao abrir a página
- controlar fluxo após autenticação

### React Router

Foi usado para criar navegação entre páginas.

Aprendizados principais:

- diferença entre App como tela e App como central de rotas
- criação de rota /
- criação de rota /dashboard
- redirecionamento de usuário não autenticado

## Aprendizados de Integração

### Comunicação Frontend e Backend

O frontend se comunica com o backend usando fetch.

Aprendizados principais:

- cada fetch chama um endpoint
- endpoint /metrics retorna métrica atual
- endpoint /metrics/historico retorna lista histórica
- uso do Authorization no cabeçalho
- leitura do JSON retornado pelo backend

### localStorage

Foi usado para salvar o token JWT no navegador.

Aprendizados principais:

- guardar token após login
- consultar token antes de liberar dashboard
- remover token futuramente no logout

## Aprendizados de Debug

Durante o projeto surgiram erros reais de ambiente e código.

Exemplos de erros enfrentados:

- Node ou npm não reconhecido
- Git sem user.name e user.email configurados
- Python não instalado ou fora do PATH
- uvloop incompatível com Windows
- biblioteca jose ausente
- erro de digitação em comandos
- erro em onChange por digitar taget em vez de target
- erro de JSX por div sem fechamento
- erro de fetch com parênteses e vírgula fora do lugar
- erro de TypeScript por uso de any
- erro de rota por componente sem return

## Linha de Pensamento para Debug

Foi praticada a análise de erro em etapas:

1. Ler a mensagem principal.
2. Identificar o arquivo e a linha indicada.
3. Entender se o erro é de ambiente, sintaxe, lógica ou tipagem.
4. Corrigir o ponto mínimo necessário.
5. Testar novamente.
6. Evitar refazer código inteiro sem entender o problema.

## Aprendizados de Git e GitHub

Foi praticado o uso de versionamento.

Aprendizados principais:

- git status
- git add
- git commit
- git push
- configuração de user.name e user.email
- criação de branch
- entendimento de Pull Request
- diferença entre main e branch de feature

## Decisões Técnicas

Algumas decisões tomadas no projeto:

- usar FastAPI para backend
- usar SQLite na fase inicial
- usar React com TypeScript no frontend
- usar JWT para autenticação
- usar Recharts para gráfico
- documentar o projeto em arquivos separados dentro da pasta docs

## Próximos Aprendizados

Os próximos pontos de evolução são:

- melhorar UI/UX
- criar logout
- formatar datas do gráfico
- separar chamadas de API em services/api.ts
- melhorar responsividade
- fazer deploy
- organizar Pull Requests
- preparar o projeto para portfólio

## Conclusão

Este projeto está sendo usado como laboratório prático para aprender desenvolvimento full stack de forma progressiva.

O foco não é apenas construir uma aplicação funcional, mas entender cada etapa, corrigir erros reais e documentar a evolução técnica.