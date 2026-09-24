# Curso Python para Análise de Dados Investigativa - Pacote Prático

Este pacote foi criado para acompanhar a apostila e o **Caso Sigma**. Todos os nomes, documentos, telefones, empresas e registros são **fictícios e didáticos**.

## Conteúdo
- 42 notebooks `.ipynb`, um para cada unidade/aula dos 5 módulos;
- scripts `.py` dos quatro projetos de módulo + projeto integrador;
- datasets CSV e JSON;
- documentos brutos TXT e PDF para mineração;
- pasta de evidências para organização e hash;
- gabaritos do instrutor;
- roteiro de aulas e testes básicos.

## Instalação
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```

## Ordem sugerida
1. `01_MODULO_FUNDAMENTOS/notebooks/`
2. `02_MODULO_MINERACAO/notebooks/`
3. `03_MODULO_PANDAS/notebooks/`
4. `04_MODULO_VISUALIZACAO/notebooks/`
5. `05_MODULO_OPERACAO_SIGMA/notebooks/`

O notebook `Caso_Sigma_Notebook_Mestre.ipynb` permite explorar rapidamente as bases.

## Dados com problemas intencionais
A base de transações contém duplicados, valores ausentes, favorecidos vazios, outliers e padrões temporais. Isso é proposital para os exercícios de limpeza, auditoria e análise.

## Observação importante
Regex identifica formato, não autenticidade. Padrões estatísticos e conexões em rede são indícios analíticos, não conclusões automáticas.
