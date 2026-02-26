# Base de Conhecimento — Zola FinPlan

Este documento descreve a base de conhecimento e o modelo de construção de contexto utilizados pela **Zola FinPlan** para projeção de **Fluxo de Caixa** e **Simulações** estruturada de cenários financeiros em horizonte de **30** dias.

## 1) Dados Utilizados

| Arquivo | Formato | Utilização no Agente |
|---|---|---|
| `data/fluxo_caixa_30d.csv` | CSV | Movimentações (entradas/saídas) para análise e projeção de liquidez |
| `data/custos_fixos.csv` | CSV | Estrutura de custos recorrentes para cálculo de pressão mensal no caixa |
| `data/metas_empresa.json` | JSON | Regras de governança: reserva mínima, prioridades e limites operacionais |
| `data/cenarios_simulacao.json` | JSON | Parâmetros para “what-if”: investimento, contratação, compra etc. |


> [!NOTE]
> **Dados mockados**: são dados fictícios e controlados, criados apenas para simular comportamentos financeiro, sem exposição de dados empresariais reais.

## 2) Adaptações e Modelagem dos Dados

### Padronizações aplicadas
- Datas em formato ISO: `YYYY-MM-DD`
- Valores numéricos em `valor` (sem símbolo de moeda)
- Tipos de lançamento: `entrada` e `saida`
- Separação entre:
  - Fluxo operacional (movimentações)
  - Estrutura fixa (custos recorrentes)
  - Regras de governaças (metas)

### Por que separar custos fixos do fluxo?
A separação permite:
- Projeção consistente de caixa (mesmo sem dados diários perfeitos)
- Comparação do “peso” estrutural sobre a receita
- Simulações mais realistas (ex.: contratação aumenta custo fixo)
- Classificação adequada da reserva mínima


## 3) Estratégia de Integração no Agente

### Carregamento de Dados
Os arquivos CSV/JSON são carregados via módulo:
`data_Loader.py`

### No início da sessão, são transformados em:
- Entradas totais do período
- Saídas totais do período
- Saldo projetado
- Total de custos fixos
- Reserva mínima configurada
  
### Construção do Contexto Calculado
Antes da chamada ao modelo, o sistema constrói um contexto determinístico contendo:
- saldo_liquido
- reserva_minima
- folga_reserva
- deficit_reserva
- reserva_ok (booleano)
  
Esse contexto é usado tanto para o painel quanto para a simulação.

### Pipeline de Processamento
A arquitetura segue um fluxo híbrido:
 1. Identificação de intenção (Simulação ou Aula)
 2. Em Simulação:
  - Parser determinístico extrai valor e tipo de ação
  - Planner classifica intenção (NOVA_SAIDA / NOVA_ENTRADA)
  - FinCalc aplica cálculo determinístico
  - Redactor gera análise apenas com base no contexto calculado
3. Em Aula:
  - Resposta estruturada e conceitual
    
### Injeção no Modelo
O modelo LLM recebe:
  - CONTEXTO_ATUAL
  - CONTEXTO_CENARIO (quando aplicável)
  - PLANO_CENARIO
  - PEDIDO_USUARIO
O modelo é instruído a:
  - Não criar novos números
  - Não recalcular valores
  - Não contradizer reserva_ok
  - Não executar transações
  - Solicitar dados quando insuficientes

## 4) Exemplo de Contexto Montado (entrada para a LLM)

```txt
Contexto (Zola FinPlan):

Horizonte: 30 dias
Reserva mínima de caixa: 8000

Fluxo de caixa (resumo):
- Entradas totais: 23900
- Saídas totais: 12160
- Saldo líquido: 11740
- Folga de reserva: 3740
- Reserva OK: true

Cenário solicitado:
- Investimento único em marketing de 1500
O modelo recebe apenas esses valores estruturados e gera análise comparativa.
```

## 5) Segurança e Limitações
- Processamento local via Ollama (sem envio para APIs externas)
- Dados fictícios para fins educacionais
- O agente não executa transações
- Não substitui contador ou consultor financeiro
- Não realiza projeções especulativas
- Quando o contexto é insuficiente, solicita parâmetros adicionais
