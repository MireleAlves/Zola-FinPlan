# Base de Conhecimento — Zola FinPlan

Este documento descreve a base de conhecimento utilizada pelo agente **Zola FinPlan**, com foco em **fluxo de caixa**, **metas**, **custos fixos** e **simulação de cenários em 30 dias**.



## 1) Dados Utilizados

| Arquivo | Formato | Utilização no Agente |
|---|---|---|
| `data/fluxo_caixa_30d.csv` | CSV | Movimentações (entradas/saídas) para análise e projeção de liquidez |
| `data/custos_fixos.csv` | CSV | Estrutura de custos recorrentes para cálculo de pressão mensal no caixa |
| `data/metas_empresa.json` | JSON | Regras de governança: reserva mínima, prioridades e limites operacionais |
| `data/cenarios_simulacao.json` | JSON | Parâmetros para “what-if”: investimento, contratação, compra etc. |


> [!NOTE]
> **Dados mockados**: são dados fictícios e controlados, criados apenas para simular comportamentos reais sem expor informações sensíveis de empresas.


## 2) Adaptações e Modelagem dos Dados

### Padronizações aplicadas
- Datas em formato ISO: `YYYY-MM-DD`
- Valores numéricos em `valor` (sem símbolo de moeda)
- Tipos de lançamento: `entrada` e `saida`
- Separação entre **fluxo operacional** e **estrutura fixa** (custos fixos)

### Por que separar custos fixos do fluxo?
Porque custos fixos permitem:
- projeção consistente de caixa (mesmo sem dados diários perfeitos)
- comparação do “peso” estrutural sobre a receita
- simulações mais realistas (ex.: contratação aumenta custo fixo)


## 3) Estratégia de Integração no Agente

### Carregamento de Dados
Os arquivos CSV/JSON são carregados no início da sessão e transformados em:
- resumo de caixa (saldo, entradas, saídas)
- total de custos fixos
- regras (metas e limites)
- catálogo de cenários para simulação

### Construção do Contexto
O agente recebe um **contexto estruturado**, com:
- visão consolidada do período (30 dias)
- regras de governança (reserva mínima e prioridades)
- cenário solicitado pelo usuário (ex.: “investir X”)

### Injeção no Modelo

A base de conhecimento é carregada dinamicamente via módulo `data_loader.py`.

O agente não utiliza dados fixos no prompt.  
Os dados são carregados, resumidos e injetados no contexto antes da chamada ao modelo.


> [!TIP]
> O agente é orientado a responder apenas com base nesse contexto e pedir dados adicionais quando necessário.


## 4) Exemplo de Contexto Montado (entrada para a LLM)

```txt
Contexto (Zola FinPlan):

Horizonte: 30 dias
Reserva mínima de caixa: 8000

Fluxo de caixa (resumo):
- Entradas totais: 23900
- Saídas totais: 12160
- Saldo projetado: 11740

Custos fixos mensais:
- Total: 5530
- Principais: Aluguel (1200), Salários (2500), Pró-labore (1200)

Cenário solicitado:
- "Aumentar marketing" (saída única de 1500)

Regras:
- Prioridade: manter liquidez
- Limite de endividamento mensal: 1500

Solicitação do usuário:
- "Zola, posso investir 1500 em marketing agora?"

```

## 5) Observações de Segurança e Escopo
- Dados mockados (não há dados bancários reais).
- O agente não executa transações.
-  Recomendações são apoio à decisão, não substituem contador/consultoria regulatória.
-  Quando o contexto for insuficiente, o agente deve responder: “Informação insuficiente” e solicitar dados.
