from pathlib import Path
import hashlib, shutil
from datetime import datetime
from collections import Counter

BASE = Path(__file__).resolve().parents[2]
origem = BASE / "dados" / "evidencias_mod1"
destino_base = BASE / "saidas" / "modulo1_organizado"

tipos = {
    ".pdf": "PDFs", ".xlsx": "Planilhas", ".csv": "Planilhas",
    ".jpg": "Imagens", ".jpeg": "Imagens", ".png": "Imagens",
    ".txt": "Logs", ".log": "Logs", ".json": "JSON"
}

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for bloco in iter(lambda: f.read(65536), b""):
            h.update(bloco)
    return h.hexdigest()

relatorio, contagem = [], Counter()
for arq in origem.iterdir():
    if not arq.is_file():
        continue
    cat = tipos.get(arq.suffix.lower(), "Outros")
    dest = destino_base / cat
    dest.mkdir(parents=True, exist_ok=True)
    shutil.copy2(arq, dest / arq.name)
    relatorio.append(f"{arq.name} | {cat} | {sha256(arq)}")
    contagem[cat] += 1

destino_base.mkdir(parents=True, exist_ok=True)
with open(destino_base / "relatorio_integridade.txt","w",encoding="utf-8") as f:
    f.write(f"Relatório gerado em {datetime.now():%d/%m/%Y %H:%M}\n\n")
    f.write("\n".join(relatorio))
    f.write("\n\nRESUMO\n")
    for k,v in sorted(contagem.items()):
        f.write(f"{k}: {v}\n")

print(f"{len(relatorio)} arquivos organizados.")
print(dict(contagem))
