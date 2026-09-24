from pathlib import Path
import sys
BASE = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(BASE))
from utils_sigma import extrair_entidades_de_pasta

entrada = BASE / "dados" / "documentos_brutos"
saida = BASE / "saidas" / "entidades_extraidas.csv"
saida.parent.mkdir(exist_ok=True)

df = extrair_entidades_de_pasta(entrada)
df.to_csv(saida, index=False, encoding="utf-8")
print(df)
print(f"\n{len(df)} entidades salvas em {saida}")
