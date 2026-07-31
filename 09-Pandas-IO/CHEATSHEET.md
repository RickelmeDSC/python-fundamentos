# 📋 Cheatsheet — Pandas I/O

Referência rápida baseada nos notebooks das aulas 01–05.

## 01 · CSV

```python
df = pd.read_csv('dados/arquivo.csv')
df = pd.read_csv(url)                            # aceita URL direto
df = pd.read_csv(arq, sep=';')                   # separador ≠ vírgula
df = pd.read_csv(arq, usecols=['a', 'b'])        # só algumas colunas
df = pd.read_csv(arq, nrows=100)                 # só as N primeiras linhas
df = pd.read_csv(arq, skiprows=3)                # pula cabeçalho sujo
df = pd.read_csv(arq, skipfooter=2, engine='python')   # skipfooter EXIGE engine='python'

df.to_csv('dados/saida.csv', index=False)        # index=False: não grava o 0,1,2...
```

## 02 · Excel e Google Sheets

```python
df = pd.read_excel('dados/planilha.xlsx')                     # precisa de openpyxl
df = pd.read_excel(arq, sheet_name='GEE Estados')             # aba pelo nome
pd.ExcelFile(arq).sheet_names                                 # listar abas sem carregar

df.to_excel('dados/saida.xlsx', index=False)
```

**Google Sheets sem API key** — via gviz:
```python
sheet_id = '1pvBoLyX8kP0...'      # trecho da URL entre /d/ e /edit
url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={nome_aba}'
df = pd.read_csv(url)             # read_CSV, não read_excel — o gviz exporta CSV
```

## 03 · JSON e APIs

```python
df = pd.read_json('dados/pacientes.json')
df.to_json('dados/saida.json')

# API → DataFrame
import requests, json
resposta = requests.get('https://jsonplaceholder.typicode.com/users')
resultado = json.loads(resposta.text)

df = pd.DataFrame(resultado)                     # colunas aninhadas viram dicts
df = pd.json_normalize(resultado, sep='_')       # ← achata: address.city → address_city
```

`json_normalize` para listas aninhadas:
```python
pd.json_normalize(dados, record_path='consultas', meta=['id', 'nome'])
# record_path: a lista que vira linhas | meta: campos do nível de cima que se repetem
```

## 04 · HTML e XML

```python
tabelas = pd.read_html('pagina.html')     # retorna LISTA de DataFrames
df = tabelas[0]                           # pegue pelo índice

df = pd.read_xml('dados/arquivo.xml')     # precisa de lxml
df.to_xml('dados/saida.xml')
df.to_html('dados/saida.html')
```

**Site bloqueia com `HTTP 403`** (Wikipedia): o urllib interno do pandas tem User-Agent genérico. Busque com requests e repasse o texto:
```python
import requests
from io import StringIO

resposta = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
df = pd.read_html(StringIO(resposta.text))[0]
```

## 05 · Banco de dados (SQLite + SQLAlchemy 2.0)

```python
from sqlalchemy import create_engine, inspect, text

engine = create_engine('sqlite:///:memory:')     # em memória — note o :memory: com DOIS ':'
engine = create_engine('sqlite:///meu.db')       # arquivo local

df.to_sql('clientes', engine, index=False)       # DataFrame → tabela
df = pd.read_sql_table('clientes', engine)       # tabela inteira
df = pd.read_sql('SELECT * FROM clientes WHERE Idade > 30', engine)   # query

inspect(engine).get_table_names()                # listar tabelas
```

**SQL cru no SQLAlchemy 2.0 — os dois obrigatórios:**
```python
query = 'UPDATE clientes SET Rendimento_anual=300000.0 WHERE ID_Cliente=6840104'
with engine.connect() as conn:
    conn.execute(text(query))     # 1) text() — string crua dá ObjectNotExecutableError
    conn.commit()                 # 2) commit() — sem ele, TUDO é revertido em silêncio
```

## ⚠️ Erros já vividos neste módulo

| Sintoma | Causa | Fix |
|---|---|---|
| `HTTP Error 403: Forbidden` | User-Agent genérico do urllib | `requests` + `StringIO` (ver aula 04) |
| `unable to open database file` | `sqlite:///memory:` sem o `:` inicial | `sqlite:///:memory:` |
| `ObjectNotExecutableError` | string crua no `conn.execute()` | envolver com `text()` |
| UPDATE/DELETE "não fez nada" | faltou `conn.commit()` | commit dentro do `with` |
| `Could not reflect: ... (Clientes)` | `read_sql_table` é case-sensitive | usar o nome exato: `'clientes'` |
| Colunas `address.city` como dict | JSON aninhado no `pd.DataFrame()` | `pd.json_normalize(..., sep='_')` |

Detalhe do último caso: SQL cru via `text()` é case-insensitive (o SQLite resolve), mas `read_sql_table` usa reflexão de metadados do SQLAlchemy — comparação exata de string.

## Dependências do módulo

`openpyxl` (Excel) · `lxml` (XML) · `html5lib` (HTML) · `sqlalchemy` (BD) · `requests` (APIs/403)
