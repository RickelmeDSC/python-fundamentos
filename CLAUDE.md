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
Fase 1 — Fundamentos (Semanas 1–3).
Estudando: Python para Dados (funções, estruturas de dados, exceções).

### Exercícios já criados
- `04_estruturas_de_dados/exercicio_01_soma_sublistas.py`
- `04_estruturas_de_dados/exercicio_02_terceiro_elemento_tuplas.py`
- `04_estruturas_de_dados/exercicio_03_lista_tuplas_posicao.py`
- `05_list_comprehensions/exercicio_04_filtro_apartamento.py`
- `06_dicionarios/exercicio_05_dict_comprehension_meses.py`

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
├── python-fundamentos           ← este repo (exercícios Fase 1)
├── dashboard-financas-pessoais  ← Projeto 1
├── ecommerce-analytics          ← Projeto 2
├── pipeline-noticias-ia         ← Projeto 3
└── agente-analista-dados        ← Projeto 4
```

## Estrutura deste repositório
```
python-fundamentos/
├── 01_variaveis_e_tipos/
├── 02_condicionais_e_loops/
├── 03_funcoes/
├── 04_estruturas_de_dados/
├── 05_list_comprehensions/
├── 06_dicionarios/
├── Skills/
├── CLAUDE.md
└── README.md
```

## Regras de código
- Python 3.11+
- Scripts rodam standalone (sem dependências externas nesta fase)
- snake_case para variáveis e funções
- Docstring no topo de cada arquivo .py
- Comentários em português (repositório de estudo)
- Apenas Python puro — sem bibliotecas externas

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
- Não instalar bibliotecas externas (Pandas, NumPy vêm depois)
- Não criar soluções complexas demais — clareza > elegância
- Não misturar exercícios de tópicos diferentes no mesmo arquivo