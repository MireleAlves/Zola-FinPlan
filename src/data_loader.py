import json
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent  # volta da pasta src para raiz do projeto
DATA_DIR = BASE_DIR / "data"

def carregar_dados():
    fluxo_caixa = pd.read_csv(DATA_DIR / "fluxo_caixa_30d.csv")
    custos_fixos = pd.read_csv(DATA_DIR / "custos_fixos.csv")

    with open(DATA_DIR / "metas_empresa.json", "r", encoding="utf-8") as f:
        metas = json.load(f)

    with open(DATA_DIR / "cenarios_simulacao.json", "r", encoding="utf-8") as f:
        cenarios = json.load(f)

    return {
        "fluxo_caixa": fluxo_caixa,
        "custos_fixos": custos_fixos,
        "metas": metas,
        "cenarios": cenarios
    }
