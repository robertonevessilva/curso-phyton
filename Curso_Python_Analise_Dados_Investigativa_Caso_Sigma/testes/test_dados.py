from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parents[1]
D = BASE/"dados"/"bases"

def test_arquivos_centrais():
    for nome in ["investigados.csv","transacoes.csv","ligacoes.csv","societario.csv","veiculos.csv","geolocalizacao.csv"]:
        assert (D/nome).exists(), nome

def test_transacoes_tem_volume():
    df=pd.read_csv(D/"transacoes.csv")
    assert len(df) > 1500

def test_dados_sao_didaticos():
    inv=pd.read_csv(D/"investigados.csv")
    assert "Aline Monteiro" in set(inv["nome"])
