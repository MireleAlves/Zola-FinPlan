<img align="left" src="assets/logo_zola_horizontal.png" width="400"/>
<br clear="left"/>

## Sobre o Projeto

A **Zola FinPlan** é um assistente de apoio à decisão financeira projetado para pequenas e médias empresas.

O sistema organiza decisões financeiras por meio de simulação estruturada de cenários, projeção de fluxo de caixa e análise comparativa controlada.

O objetivo é transformar dados financeiros em **decisões mais previsíveis e menos impulsivas**.

## Problema

Pequenas empresas frequentemente tomam decisões financeiras sem projeção clara de liquidez.

Decisões como:

- contratar um funcionário
- investir em marketing
- realizar uma compra relevante

são feitas sem simulação estruturada do impacto no caixa.

Isso pode gerar:

- comprometimento do caixa
- perda da reserva mínima
- aumento do risco operacional
- falta de previsibilidade financeira

## Solução

A Zola FinPlan organiza decisões financeiras através de três camadas principais:

1. **Cálculo determinístico do fluxo de caixa (30 dias)**
2. **Simulação estruturada de cenários**
3. **Análise comparativa gerada por modelo de linguagem controlado**

Os cálculos financeiros são realizados diretamente pelo sistema.

O modelo de linguagem atua apenas na interpretação do contexto já calculado, reduzindo risco de inconsistências.

## Demonstração

Durante a demonstração são apresentados:

- painel financeiro com fluxo de caixa
- simulação de cenários financeiros
- análise de risco de liquidez
- modo explicação de conceitos financeiros

### Vídeo de apresentação:

&rarr; https://drive.google.com/file/d/1Ymqs6nyEtL0k-JznxqyVB39UitN2dZs-/view?usp=drive_link

## Arquitetura da Solução

A Zola FinPlan utiliza uma arquitetura híbrida composta por:

- **Cálculo determinístico em Python**
- **Interface interativa com Streamlit**
- **Modelo local executado via Ollama**
- **Base de conhecimento estruturada em CSV e JSON**

Essa abordagem reduz alucinações e mantém coerência nas análises financeiras.

## Funcionalidades

- Simulação de decisões financeiras
- Projeção de fluxo de caixa (30 dias)
- Validação de reserva mínima
- Classificação de risco de liquidez
- Explicação de conceitos financeiros
- Interface conversacional

## Tecnologias Utilizadas

- Python
- Streamlit
- Pandas
- Ollama (LLM local)
- JSON / CSV (base de conhecimento)

## Como Executar

&rarr; Instalar dependências

```bash
pip install streamlit pandas requests
ollama run llama3
streamlit run src/app.py
```

## Proposta de Valor

A **Zola FinPlan** orpaniza decisões financeiras antes da execução.

Isso permite:
- maior previsibilidade operacional
- redução de risco de liquidez
- apoio estruturado à tomada de decisão
 
 ## Zola

Infraestrutura para a Inteligência Empresarial
