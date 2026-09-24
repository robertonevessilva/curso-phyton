from pathlib import Path
import pandas as pd
import networkx as nx

BASE=Path(__file__).resolve().parents[1]
dados=BASE/"dados"/"bases"

t=pd.read_csv(dados/"transacoes.csv")
t["valor"]=pd.to_numeric(t["valor"],errors="coerce")
print("Ex. 9 - top favorecidos")
print(t.groupby("favorecido")["valor"].sum().nlargest(5))

inv=pd.read_csv(dados/"investigados.csv",dtype={"cpf":str})
v=pd.read_csv(dados/"veiculos.csv",dtype={"cpf_proprietario":str})
cv=inv.merge(v,left_on="cpf",right_on="cpf_proprietario",how="inner")
print("\nEx. 10 - investigados com mais de um veículo")
print(cv.groupby(["cpf","nome_x"]).size().loc[lambda s:s>1])

lig=pd.read_csv(dados/"ligacoes.csv")
G=nx.from_pandas_edgelist(lig,"origem","destino")
print("\nEx. 15 - hubs")
print(sorted(nx.degree_centrality(G).items(),key=lambda x:x[1],reverse=True)[:5])
