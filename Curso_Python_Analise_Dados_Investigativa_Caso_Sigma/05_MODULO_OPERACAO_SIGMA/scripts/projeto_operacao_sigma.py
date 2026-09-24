from pathlib import Path
import sys, pandas as pd

BASE = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(BASE))
from utils_sigma import extrair_entidades_de_pasta

dados = BASE/"dados"
saida = BASE/"saidas"/"operacao_sigma"
saida.mkdir(parents=True, exist_ok=True)

# 1. Extração
ent = extrair_entidades_de_pasta(dados/"documentos_brutos")
ent.to_csv(saida/"entidades_extraidas.csv", index=False)

# 2. Cruzamento financeiro-societário
fin = pd.read_csv(dados/"bases"/"financeiro.csv", dtype={"cpf":str})
soc = pd.read_csv(dados/"bases"/"societario.csv", dtype={"cpf":str})
fin["valor"] = pd.to_numeric(fin["valor"], errors="coerce")
cruz = fin.merge(soc, on="cpf", how="inner", suffixes=("_fin","_soc"))
resumo = cruz.groupby(["cpf","nome_soc","razao_social"])["valor"].agg(["sum","count"]).reset_index()
resumo.to_csv(saida/"cruzamento_financeiro_societario.csv", index=False)

# 3. Hipótese: grandes volumes e vínculos societários
priorizados = resumo[(resumo["sum"] >= 50000) | (resumo["count"] >= 20)].sort_values("sum", ascending=False)
priorizados.to_csv(saida/"achados_priorizados.csv", index=False)

print("Entidades extraídas:", len(ent))
print("Coincidências financeiro-societárias:", len(cruz))
print("\nAchados priorizados:")
print(priorizados.head(20))
