from pathlib import Path
import re
import pandas as pd
import hashlib

PADROES = {
    "CPF": r"\d{3}\.\d{3}\.\d{3}-\d{2}",
    "CNPJ": r"\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}",
    "Telefone": r"\(\d{2}\)\s?\d{4,5}-\d{4}",
    "Email": r"[\w.\-]+@[\w.\-]+\.\w+",
    "Placa": r"\b[A-Z]{3}-?\d[A-Z0-9]\d{2}\b",
    "Data": r"\b\d{2}/\d{2}/\d{4}\b",
    "Processo": r"\b\d{7}-\d{2}\.\d{4}\.\d\.\d{2}\.\d{4}\b",
}

def calcular_hash(caminho):
    h = hashlib.sha256()
    with open(caminho, "rb") as f:
        for bloco in iter(lambda: f.read(65536), b""):
            h.update(bloco)
    return h.hexdigest()

def extrair_texto(caminho):
    caminho = Path(caminho)
    if caminho.suffix.lower() == ".pdf":
        import pdfplumber
        texto = ""
        with pdfplumber.open(caminho) as pdf:
            for pagina in pdf.pages:
                texto += (pagina.extract_text() or "") + "\n"
        return texto
    return caminho.read_text(encoding="utf-8", errors="ignore")

def extrair_entidades_de_pasta(pasta):
    resultados = []
    for arquivo in Path(pasta).iterdir():
        if arquivo.suffix.lower() not in {".txt",".pdf",".log"}:
            continue
        texto = extrair_texto(arquivo)
        for tipo, padrao in PADROES.items():
            for achado in sorted(set(re.findall(padrao, texto, flags=re.I))):
                resultados.append({"arquivo_origem": arquivo.name, "tipo_entidade": tipo, "valor_encontrado": achado})
    return pd.DataFrame(resultados)
