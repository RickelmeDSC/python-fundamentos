# Python Fundamentos

Repositório de exercícios e estudos de Python de um roadmap estruturado de 22 semanas em transição de carreira para **Análise de Dados + IA + Automação**. Cobre a **Fase 1 completa** e está em andamento na **Fase 2** (Semana 4).

---

## Sobre

Este repositório cobre os fundamentos de Python com foco em Dados: sintaxe, estruturas, funções, estatística e, a partir da Fase 2, Pandas para leitura/escrita de diferentes formatos de arquivo. Os scripts da Fase 1 (pastas `01-` a `08-`) rodam standalone com Python puro — sem dependências externas. A partir da Fase 2 (`09-Pandas-IO/` em diante), bibliotecas como pandas, sqlalchemy e requests passam a ser usadas — veja o README de cada módulo para a lista exata.

---

## Roadmap

| Fase | Semanas | Foco | Projeto final |
|------|---------|------|---------------|
| Fase 1 — Fundamentos | 1–3 | Python, SQL (SQLite), Estatística, Pandas intro | Dashboard de Finanças Pessoais |
| **Fase 2 — Ferramentas** | 4–7 | Pandas completo, SQL joins, Power BI, DAX | Análise E-commerce (Olist) |
| Fase 3 — Profissionalização | 8–13 | BigQuery, APIs, n8n, Make, IA aplicada | Pipeline de Notícias com IA |
| Fase 4 — Diferenciação | 14–22 | Claude API, LangChain, RAG, LangGraph, ML, MLOps | Agente Analista Autônomo |

---

## Estrutura

```
python-fundamentos/ 
├── 01-Variaveis-e-Tipos/          ← vazia por enquanto
├── 02-Condicionais-e-Loops/       ← vazia por enquanto
├── 03-Funcoes/                    ← vazia por enquanto
├── 04-Estrutura-De-Dados/
│   ├── exercicio_01_soma_sublistas.py
│   ├── exercicio_02_terceiro_elemento_tuplas.py
│   └── exercicio_03_lista_tuplas_posicao.py
├── 05-ListComprehensions/
│   ├── exercicio_04_filtro_apartamento.py
│   ├── exercicio_06_filtro_vendas_2022.py
│   ├── exercicio_07_rotulo_glicemia.py
│   └── exercicio_08_tabela_ecommerce.py
├── 06-Dicionarios/
│   ├── exercicio_05_dict_comprehension_meses.py
│   ├── exercicio_09_contagem_filiais.py
│   └── exercicio_10_soma_funcionarios_por_estado.py
├── 07-Excecoes/
│   ├── exercicio_11_divisao_com_excecoes.py
│   ├── exercicio_12_busca_dicionario.py
│   ├── exercicio_13_converte_lista_float.py
│   ├── exercicio_14_agrupa_listas_tuplas.py
│   ├── desafio_01_pontuacao_estudantes.py
│   ├── desafio_02_verificacao_pontuacao_nlp.py
│   └── desafio_03_divide_colunas.py
├── 08-Estatistica/
│   ├── 01_distribuicao_frequencia.py
│   ├── 02_tendencia_central.py
│   ├── 03_separatrizes.py
│   └── 04_dispersao.py
├── 09-Pandas-IO/          ← Fase 2 — ver README próprio (dependências e status)
│   ├── 01_csv/
│   ├── 02_excel/
│   ├── 03_json/
│   ├── 04_html_xml/
│   └── 05_banco_dados/
└── 10-Pandas-Selecionando-Agrupando/   ← Fase 2 — ver README próprio (dados e status)
    ├── 01_conhecendo_os_dados/
    ├── 02_agrupamento_de_dados/
    ├── 03_agrupamentos_multi_index/
    └── 04_unindo_dados/
```

> 📋 Cada módulo com conteúdo (`04-` em diante) tem um **`CHEATSHEET.md`** — referência rápida dos métodos e armadilhas vistos no módulo, baseada nos próprios exercícios.

---

## Exercícios

### 04-Estrutura-De-Dados
| # | Descrição | Conceitos |
|---|-----------|-----------|
| 01 | Soma dos elementos de cada sublista | `for`, `sum()`, listas aninhadas |
| 02 | Terceiro elemento de cada tupla em uma lista | indexação de tuplas, list comprehension |
| 03 | Lista de tuplas `(posição, nome)` a partir de uma lista | `enumerate()`, tuplas |

### 05-ListComprehensions
| # | Descrição | Conceitos |
|---|-----------|-----------|
| 04 | Filtrar valores de tuplas pelo tipo (`'Apartamento'`) | list comprehension com `if` |
| 06 | Filtrar vendas de 2022 com valor acima de 6000 | list comprehension com `and` |
| 07 | Classificar valores de glicemia em rótulos clínicos | expressão ternária aninhada |
| 08 | Montar tabela de vendas e-commerce com cabeçalho e total | `zip()`, cálculo inline, list comprehension |

### 06-Dicionarios
| # | Descrição | Conceitos |
|---|-----------|-----------|
| 05 | Dicionário mês → despesa com dict comprehension | `zip()`, dict comprehension |
| 09 | Contar filiais por estado | `set()`, dict comprehension, passo intermediário |
| 10 | Agrupar e somar colaboradores por estado | dict comprehension encadeado, `.items()` |

### 07-Excecoes
| # | Descrição | Conceitos |
|---|-----------|-----------|
| 11 | Divisão com tratamento de `ValueError` e `ZeroDivisionError` | `try/except` múltiplo, `type(e).__name__` |
| 12 | Busca em dicionário com tratamento de `KeyError` | `try/except KeyError`, input do usuário |
| 13 | Converte lista para float com `finally` | `try/except/finally`, função com retorno condicional |
| 14 | Agrupa duas listas em tuplas com `raise` manual | `raise`, `IndexError`, `TypeError` |

### 07-Excecoes — Desafios
| # | Descrição | Conceitos |
|---|-----------|-----------|
| 01 | Pontuação de estudantes com validação de alternativas | `raise ValueError`, validação pré-cálculo, `zip()` |
| 02 | Verificação de pontuações em texto NLP | `raise ValueError`, `in`, `or`, pré-processamento |
| 03 | Divisão de colunas experimentais (pressão/temperatura) | `try/except` duplo, `ValueError`, `ZeroDivisionError` |

### 08-Estatistica

> ⚠️ **Pendente:** os arquivos `.py` deste módulo estão vazios — os tópicos abaixo ainda aguardam implementação. O [`CHEATSHEET.md`](08-Estatistica/CHEATSHEET.md) do módulo já cobre a teoria.

| # | Descrição | Conceitos |
|---|-----------|-----------|
| 01 | Distribuição de frequência | classes, frequência absoluta/relativa |
| 02 | Medidas de tendência central | média, mediana, moda |
| 03 | Separatrizes | quartis, decis, percentis |
| 04 | Medidas de dispersão | variância, desvio padrão, coeficiente de variação |

---

## 09-Pandas-IO (Fase 2)

Módulo separado — curso Alura "Pandas I/O: trabalhando com diferentes formatos de arquivos". Cobre leitura/escrita de CSV, Excel, JSON, HTML/XML e banco de dados (SQLite via SQLAlchemy).

Como esse módulo usa dependências externas (pandas, sqlalchemy, requests, etc.), a lista completa de pacotes e o status de cada aula estão em [`09-Pandas-IO/README.md`](09-Pandas-IO/README.md).

---

## 10-Pandas-Selecionando-Agrupando (Fase 2)

Módulo separado — curso Alura "Pandas: selecionando e agrupando dados". Cobre `loc`/`iloc`/`query`, `groupby` com múltiplas agregações, `MultiIndex` e `merge`/`join`/`concat`.

O dataset (planilha do SEEG, ~78 MB) **não é versionado**. As instruções de download e o status de cada aula estão em [`10-Pandas-Selecionando-Agrupando/README.md`](10-Pandas-Selecionando-Agrupando/README.md).

---

## Como executar

Qualquer script pode ser executado diretamente:

```bash
py 04-Estrutura-De-Dados/exercicio_01_soma_sublistas.py
```

Requisito: **Python 3.11+**

> No Windows, use `py` — o comando `python` pode ser interceptado pelo alias da Microsoft Store quando o Python não foi instalado por ela.

---

## Convenções

- `snake_case` para variáveis e funções
- Docstring no topo de cada arquivo
- Comentários em português
- Cada módulo com conteúdo tem um `CHEATSHEET.md` de consulta rápida
- Fase 1 (pastas `01-` a `08-`): apenas Python puro, sem bibliotecas externas
- Fase 2 em diante (`09-Pandas-IO/` e módulos seguintes): bibliotecas documentadas no README de cada módulo

---

## Repositórios do roadmap

| Repositório | Fase | Status |
|-------------|------|--------|
| [python-fundamentos](https://github.com/RickelmeDSC/python-fundamentos) | Fase 1-2 | Em andamento |
| dashboard-financas-pessoais | Fase 1 | Pendente |
| ecommerce-analytics | Fase 2 | Pendente |
| pipeline-noticias-ia | Fase 3 | Pendente |
| agente-analista-dados | Fase 4 | Pendente |
