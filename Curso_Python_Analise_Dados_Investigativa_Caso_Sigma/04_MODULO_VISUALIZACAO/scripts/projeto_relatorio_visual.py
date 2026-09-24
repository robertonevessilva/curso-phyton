from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import folium
from folium.plugins import HeatMap
import networkx as nx

BASE = Path(__file__).resolve().parents[2]
dados = BASE/"dados"/"bases"
saida = BASE/"saidas"/"visual"
saida.mkdir(parents=True, exist_ok=True)

# Gráfico
t = pd.read_csv(dados/"transacoes.csv")
t["valor"] = pd.to_numeric(t["valor"], errors="coerce")
top = t.groupby("nome")["valor"].sum().sort_values(ascending=False).head(8)
ax = top.plot(kind="bar", title="Valor total movimentado por alvo")
ax.set_ylabel("Valor (R$)")
plt.tight_layout()
plt.savefig(saida/"grafico_valores.png", dpi=160)
plt.close()

# Mapa
pts = pd.read_csv(dados/"pontos_interesse.csv")
mapa = folium.Map(location=[-8.0476,-34.8770], zoom_start=12)
for _,r in pts.iterrows():
    folium.Marker([r.latitude,r.longitude], popup=f"{r['nome']} ({r['tipo']})").add_to(mapa)
mapa.save(saida/"mapa_investigativo.html")

# Heatmap
occ = pd.read_csv(dados/"ocorrencias.csv")
mh = folium.Map(location=[-8.0476,-34.8770], zoom_start=12)
HeatMap(occ[["latitude","longitude"]].values.tolist(), radius=15).add_to(mh)
mh.save(saida/"mapa_de_calor.html")

# Rede
lig = pd.read_csv(dados/"ligacoes.csv")
G = nx.Graph()
for _,r in lig.iterrows():
    G.add_edge(r.origem, r.destino)
cent = nx.degree_centrality(G)
ranking = sorted(cent.items(), key=lambda x:x[1], reverse=True)
plt.figure(figsize=(11,8))
nx.draw(G, with_labels=True, node_size=900, font_size=7)
plt.tight_layout()
plt.savefig(saida/"rede_contatos.png", dpi=160)
plt.close()

# Dashboard
html = f"""<html><head><meta charset='utf-8'><title>Caso Sigma</title></head>
<body style='font-family:Arial;max-width:1100px;margin:auto'>
<h1>Relatório Visual Interativo - Caso Sigma</h1>
<p>Material didático fictício.</p>
<h2>Mapa de pontos</h2><iframe src='mapa_investigativo.html' width='100%' height='500'></iframe>
<h2>Mapa de calor</h2><iframe src='mapa_de_calor.html' width='100%' height='500'></iframe>
<h2>Rede de contatos</h2><img src='rede_contatos.png' style='max-width:100%'>
<h2>Ranking de centralidade</h2><pre>{ranking[:10]}</pre>
</body></html>"""
(saida/"dashboard_final.html").write_text(html,encoding="utf-8")
print("Arquivos gerados em", saida)
