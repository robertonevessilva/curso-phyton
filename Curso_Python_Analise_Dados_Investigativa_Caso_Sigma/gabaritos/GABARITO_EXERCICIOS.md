# Gabarito orientativo - Exercícios 1 a 16

Todos os dados deste pacote são fictícios. O gabarito privilegia método e auditabilidade; soluções equivalentes são aceitáveis.

## Módulo 1
**1.** Criar variáveis `nome`, `cpf` (str) e `qtd_telefones`; usar f-string.  
**2.** Função com `sum(1 for v in valores if v >= 10000)`.  
**3.** Usar `Counter`/dicionário para contar categorias no Organizador.  
**4.** Hashes de arquivos idênticos devem coincidir; qualquer alteração no conteúdo muda o SHA-256.

## Módulo 2
**5.** Regex sugerido: `r"\b\d{2}/\d{2}/\d{4}\b"`.  
**6.** Use `unicodedata.normalize("NFKD", texto)` e remova caracteres combinantes.  
**7.** Adicione `Email` com padrão semelhante a `r"[\w.\-]+@[\w.\-]+\.\w+"`.  
**8.** Validar o padrão didático contra a especificação oficial antes de uso real; regex localiza formato, não autenticidade.

## Módulo 3
**9.** `groupby("favorecido")["valor"].sum().nlargest(5)`.  
**10.** `merge` por CPF e depois `groupby("cpf").size()`; P001 e P008 têm mais de um veículo no dataset.  
**11.** Converter `data`, definir índice e usar `resample`; compare janelas ao redor dos feriados escolhidos.  
**12.** Função pode combinar valor e frequência; documentar os limiares.

## Módulo 4
**13.** `resample("M")` ou agrupamento por mês e `plot(kind="line")`.  
**14.** Use `pontos_interesse.csv`; diferencie por `tipo`.  
**15.** Construa `Graph`, calcule `nx.degree_centrality` e ordene.  
**16.** Gere HTML reunindo mapa e imagem do gráfico/rede.

## Módulo 5 - chaves pedagógicas do Caso Sigma
Há padrões deliberadamente plantados: concentração de repasses para ALFA em sextas/sábados, valores frequentemente próximos de R$ 10 mil, alguns outliers financeiros, vínculos societários cruzáveis e encontros simulados na ERB4521 entre duas linhas em datas específicas. O aluno deve descobrir os padrões pelo método, não receber esta lista antes da atividade.
