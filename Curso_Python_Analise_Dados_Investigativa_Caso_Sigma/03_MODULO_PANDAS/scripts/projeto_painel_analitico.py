from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parents[2]
dados = BASE / "dados" / "bases"
saida = BASE / "saidas"
saida.mkdir(exist_ok=True)

trans = pd.read_csv(dados/"transacoes.csv", dtype={"cpf":str})
inv = pd.read_csv(dados/"investigados.csv", dtype={"cpf":str})

trans["valor"] = pd.to_numeric(trans["valor"], errors="coerce")
qtd_inicial = len(trans)
duplicadas = trans.duplicated().sum()
trans = trans.drop_duplicates()
sem_valor = trans["valor"].isna().sum()
trans = trans.dropna(subset=["valor"])
trans["favorecido"] = trans["favorecido"].fillna("NÃO INFORMADO").replace("", "NÃO INFORMADO")

resumo = trans.groupby("cpf")["valor"].agg(["sum","mean","count"]).reset_index()
resumo.columns = ["cpf","total_movimentado","valor_medio","qtd_transacoes"]
limites = resumo.assign(limite_atipico=resumo["valor_medio"]*3)[["cpf","limite_atipico"]]
trans = trans.merge(limites,on="cpf",how="left")
anomalias = trans[trans["valor"] > trans["limite_atipico"]].copy()
painel = resumo.merge(inv[["cpf","nome","prioridade"]], on="cpf", how="left")

painel.to_csv(saida/"painel_analitico.csv", index=False)
anomalias.to_csv(saida/"transacoes_atipicas.csv", index=False)
print(f"Inicial: {qtd_inicial} | duplicadas removidas: {duplicadas} | sem valor removidas: {sem_valor}")
print(painel.sort_values("total_movimentado", ascending=False).head(10))
