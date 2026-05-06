# Fluxo do Dashboard — Dashboard Insta Analytics

## Objetivo

Este documento explica como a tela de dashboard funciona no projeto.

O dashboard é responsável por exibir métricas atuais e históricas de forma visual, usando dados vindos do backend.

## Arquivo Principal

Frontend:

- frontend/src/pages/DashboardPage.tsx

## Responsabilidades do Dashboard

A tela de dashboard é responsável por:

- verificar se o usuário está autenticado
- impedir acesso sem token
- buscar métricas atuais
- buscar histórico de métricas
- exibir cards com indicadores principais
- exibir gráfico de evolução de seguidores

## Fluxo Geral

1. Usuário acessa /dashboard.
2. Frontend verifica se existe token no localStorage.
3. Se não existir token, usuário volta para login.
4. Se existir token, frontend faz requisições para o backend.
5. Backend valida o Bearer Token.
6. Backend retorna dados em JSON.
7. Frontend salva os dados no estado.
8. React renderiza cards e gráfico.

## Proteção da Tela

Antes de mostrar os dados, o Dashboard verifica se existe token salvo.

Se não houver token, o usuário é redirecionado para:

- /

Essa proteção impede que usuários não autenticados acessem diretamente a tela do dashboard.

## Métricas Atuais

Endpoint utilizado:

- GET /metrics

Esse endpoint retorna a métrica atual do sistema.

Dados exibidos atualmente:

- seguidores
- alcance
- impressões

Esses dados são exibidos em cards visuais.

## Histórico de Métricas

Endpoint utilizado:

- GET /metrics/historico

Esse endpoint retorna uma lista de registros históricos.

Cada registro contém informações como:

- seguidores
- alcance
- impressões
- data de criação
- dados de engajamento

O histórico é usado para alimentar o gráfico de evolução.

## Estados Usados no Frontend

O Dashboard usa estados do React para controlar os dados da tela.

### metric

Guarda a métrica atual retornada pelo endpoint /metrics.

### historico

Guarda a lista histórica retornada pelo endpoint /metrics/historico.

### loading

Controla se os dados ainda estão carregando.

## Renderização Condicional

A tela muda de acordo com o estado dos dados.

Se loading for verdadeiro:

- mostra mensagem de carregamento

Se não houver métrica:

- mostra mensagem informando que nenhuma métrica foi encontrada

Se houver métrica:

- mostra cards com os dados

Se houver histórico:

- mostra gráfico com evolução de seguidores

## Gráfico

A visualização gráfica usa a biblioteca Recharts.

O gráfico atual mostra:

- eixo X: data de criação da métrica
- eixo Y: quantidade de seguidores

Esse gráfico ajuda a visualizar a evolução dos dados ao longo do tempo.

## Fluxo Resumido

Usuário acessa dashboard  
↓  
Dashboard verifica token  
↓  
Frontend busca /metrics  
↓  
Frontend busca /metrics/historico  
↓  
Backend valida token  
↓  
Backend retorna JSON  
↓  
React salva dados no estado  
↓  
Cards e gráfico são exibidos  

## Possíveis Melhorias Futuras

- formatar datas no eixo do gráfico
- adicionar múltiplas linhas no gráfico
- exibir alcance e impressões no gráfico
- criar filtros por período
- criar botão de logout
- melhorar layout visual
- separar cards em componentes próprios
- criar serviço de API separado no frontend
- melhorar tratamento de erro

## Aprendizado Principal

O fluxo do dashboard mostra como dados protegidos podem ser consumidos no frontend e transformados em visualizações úteis para o usuário.

Esse padrão é comum em sistemas de analytics, BI, CRMs, ERPs, plataformas SaaS e painéis administrativos.