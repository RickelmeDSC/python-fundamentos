# CLAUDE.md — Contexto do Projeto

## Quem sou
Ricklelme (RickelmeDSC). Estou em transição de carreira para Análise de Dados + IA + Automação, seguindo um roadmap estruturado de 22 semanas.

## Roadmap — Visão geral

| Fase | Semanas | Foco | Projeto final |
|------|---------|------|---------------|
| Fase 1 — Fundamentos | 1–3 | Python, SQL (SQLite), Estatística, Pandas intro | Dashboard de Finanças Pessoais |
| Fase 2 — Ferramentas | 4–7 | Pandas completo, SQL joins, Power BI, DAX | Análise E-commerce (Olist) |
| Fase 3 — Profissionalização | 8–13 | BigQuery, APIs, n8n, Make, IA aplicada | Pipeline de Notícias com IA |
| Fase 4 — Diferenciação | 14–22 | Claude API, LangChain, RAG, LangGraph, ML, MLOps | Agente Analista Autônomo |

## Fase atual
Fase 2 — Ferramentas (Semana 4). Fase 1 (Fundamentos) concluída.
Estudando: Pandas — selecionando e agrupando dados (`loc`/`iloc`/`query`, `groupby`, `MultiIndex`, `merge`/`join`/`concat`). Pandas I/O concluído.

### Fase 1 — Exercícios já criados
- `04-Estrutura-De-Dados/exercicio_01_soma_sublistas.py`
- `04-Estrutura-De-Dados/exercicio_02_terceiro_elemento_tuplas.py`
- `04-Estrutura-De-Dados/exercicio_03_lista_tuplas_posicao.py`
- `05-ListComprehensions/exercicio_04_filtro_apartamento.py`
- `06-Dicionarios/exercicio_05_dict_comprehension_meses.py`
- `05-ListComprehensions/exercicio_06_filtro_vendas_2022.py`
- `05-ListComprehensions/exercicio_07_rotulo_glicemia.py`
- `05-ListComprehensions/exercicio_08_tabela_ecommerce.py`
- `06-Dicionarios/exercicio_09_contagem_filiais.py`
- `06-Dicionarios/exercicio_10_soma_funcionarios_por_estado.py`
- `07-Excecoes/exercicio_11_divisao_com_excecoes.py`
- `07-Excecoes/exercicio_12_busca_dicionario.py`
- `07-Excecoes/exercicio_13_converte_lista_float.py`
- `07-Excecoes/exercicio_14_agrupa_listas_tuplas.py`

### Fase 1 — Desafios já criados
- `07-Excecoes/desafio_01_pontuacao_estudantes.py`
- `07-Excecoes/desafio_02_verificacao_pontuacao_nlp.py`
- `07-Excecoes/desafio_03_divide_colunas.py`

### Fase 1 — Estatística (`08-Estatistica/`)
**⚠️ Pendência:** os quatro arquivos abaixo existem mas estão **vazios (0 bytes)** desde o commit inicial — o conteúdo nunca foi implementado. O `CHEATSHEET.md` do módulo cobre a teoria prevista.
- `01_distribuicao_frequencia.py`
- `02_tendencia_central.py`
- `03_separatrizes.py`
- `04_dispersao.py`

### Fase 2 — Pandas I/O (`09-Pandas-IO/`)
Curso Alura "Pandas I/O: trabalhando com diferentes formatos de arquivos". Dependências extras documentadas em `09-Pandas-IO/README.md`.
- `01_csv/` — leitura/escrita de CSV (concluído)
- `02_excel/` — Excel e Google Sheets (concluído)
- `03_json/` — JSON aninhado e normalização de resposta de API (concluído)
- `04_html_xml/` — tabelas HTML (Wikipedia) e XML (concluído)
- `05_banco_dados/` — SQLite via SQLAlchemy, CRUD (concluído)

### Fase 2 — Pandas selecionando e agrupando (`10-Pandas-Selecionando-Agrupando/`)
Curso Alura "Pandas: selecionando e agrupando dados" (Nível 1 #16). Dataset: planilha SEEG (~78 MB, aba `GEE Estados`) — **não versionada**, instruções de download em `10-Pandas-Selecionando-Agrupando/README.md`.
- `01_conhecendo_os_dados/` — concluído
- `02_agrupamento_de_dados/` — concluído (melt, groupby, agregações, desafio hora da prática)
- `03_agrupamentos_multi_index/` — em andamento (xs, swaplevel, idxmax/insert, pivot_table com aggfunc, desafios)
- `04_unindo_dados/` — pendente

## Stack completa do roadmap (em ordem de aprendizado)
- **Linguagem:** Python 3.11+
- **SQL:** SQLite (fundamentos) → BigQuery (cloud)
- **Dados:** Pandas, NumPy
- **Visualização:** Matplotlib, Seaborn, Power BI + DAX
- **Automação:** n8n, Make
- **APIs:** Requests, REST
- **IA/LLM:** API Anthropic (Claude), LangChain, LangGraph
- **RAG:** MongoDB Atlas (Vector Search), embeddings
- **ML:** Scikit-learn
- **Observabilidade:** MLFlow
- **Deploy:** Streamlit, FastAPI, Render

## Decisões estratégicas já tomadas
- SQLite + BigQuery (MySQL foi descartado — redundante)
- LangChain + Anthropic API (LlamaIndex foi descartado)
- Power BI como ferramenta de BI principal (QuickSight descartado)
- Cursos extras Anthropic + Python e Governança de IA são tratados como essenciais

## Repositórios planejados
```
github.com/RickelmeDSC/
├── python-fundamentos           ← este repo (exercícios Fase 1-2)
├── dashboard-financas-pessoais  ← Projeto 1
├── ecommerce-analytics          ← Projeto 2
├── pipeline-noticias-ia         ← Projeto 3
└── agente-analista-dados        ← Projeto 4
```

## Estrutura deste repositório
```
python-fundamentos/
├── 01-Variaveis-e-Tipos/
├── 02-Condicionais-e-Loops/
├── 03-Funcoes/
├── 04-Estrutura-De-Dados/
├── 05-ListComprehensions/
├── 06-Dicionarios/
├── 07-Excecoes/
├── 08-Estatistica/
├── 09-Pandas-IO/
│   ├── 01_csv/
│   ├── 02_excel/
│   ├── 03_json/
│   ├── 04_html_xml/
│   ├── 05_banco_dados/
│   └── README.md        ← dependências extras e status das aulas
├── 10-Pandas-Selecionando-Agrupando/
│   ├── 01_conhecendo_os_dados/
│   ├── 02_agrupamento_de_dados/
│   ├── 03_agrupamentos_multi_index/
│   ├── 04_unindo_dados/
│   └── README.md        ← download do dataset SEEG e status das aulas
├── Skills/
├── CLAUDE.md
└── README.md
```

## Regras de código
- Python 3.11+ (nesta máquina o interpretador é chamado com `py`, não `python`)
- snake_case para variáveis e funções
- Docstring no topo de cada arquivo .py
- Comentários em português (repositório de estudo)
- Cada módulo com conteúdo (`04-` em diante) tem um `CHEATSHEET.md` de referência rápida — ao concluir novas aulas/exercícios, atualizar o cheatsheet do módulo correspondente

### Fase 1 (pastas `01-` a `08-`)
- Apenas Python puro — sem bibliotecas externas

### Fase 2 em diante (`09-Pandas-IO/` e módulos seguintes)
- Bibliotecas usadas são as documentadas no README de cada módulo (ex.: `09-Pandas-IO/README.md` lista pandas, openpyxl, lxml, html5lib, sqlalchemy, requests)
- Não instalar nada além do que já está listado nesses READMEs sem confirmar antes

## Convenções de commit
- `feat: adiciona exercícios de [tópico]`
- `fix: corrige exercício [número] de [tópico]`
- `docs: atualiza README`
- `refactor: melhora solução de [tópico]`

## Como me ajudar
- Explicar o conceito antes de mostrar a solução
- Dar dicas antes de dar resposta pronta
- Se meu código funciona mas pode melhorar, elogie primeiro e sugira depois
- Conectar o exercício com aplicação real em dados quando possível
- Não gerar soluções completas sem que eu tente primeiro
- Responder em português

## O que NÃO fazer
- Não instalar bibliotecas fora das documentadas para a fase/módulo atual (ver "Regras de código" acima)
- Não criar soluções complexas demais — clareza > elegância
- Não misturar exercícios de tópicos diferentes no mesmo arquivo