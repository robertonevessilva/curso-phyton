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

### GitHub Codespaces

1. Abra o repositório no GitHub e escolha **Code > Codespaces > Create codespace on main**.
2. Aguarde a criação do ambiente. O Codespace instala automaticamente as dependências e registra o kernel `Python (Curso Sigma)`.
3. Abra um notebook e selecione `Python (Curso Sigma)` no seletor de kernel no canto superior direito.
4. Execute as células na ordem. Não use um kernel global diferente do kernel do curso.

### VS Code local

Na raiz do repositório, execute:

```bash
python3.11 -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r Curso_Python_Analise_Dados_Investigativa_Caso_Sigma/requirements.txt
python -m ipykernel install --user --name curso-python-investigativa --display-name "Python (Curso Sigma)"
jupyter notebook
```

No VS Code, selecione o interpretador `.venv/bin/python` (ou `.venv\\Scripts\\python.exe` no Windows) e, em cada notebook, selecione o kernel `Python (Curso Sigma)`.

Se o computador não tiver Python 3.11, use o arquivo `environment.yml` com Conda/Mamba:

```bash
conda env create -f Curso_Python_Analise_Dados_Investigativa_Caso_Sigma/environment.yml
conda activate curso-python-investigativa
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
