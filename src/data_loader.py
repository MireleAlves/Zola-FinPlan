import json
import pandas as pd

def carregar_dados():
    dados = {}

    # CSVs
    dados["transacoes"] = pd.read_csv("data/transacoes.csv")
    dados["fluxo_30d"] = pd.read_csv("data/fluxo_caixa_30d.csv")

    # JSONs
    with open("data/perfil_empresa.json", "r", encoding="utf-8") as f:
        dados["perfil_empresa"] = json.load(f)

    with open("data/metas_empresa.json", "r", encoding="utf-8") as f:
        dados["metas"] = json.load(f)

    with open("data/parametros_financeiros.json", "r", encoding="utf-8") as f:
        dados["parametros"] = json.load(f)

    return dados
