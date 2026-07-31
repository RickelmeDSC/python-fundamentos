# 📋 Cheatsheet — Pandas: selecionando e agrupando

Referência rápida. Exemplos em cima do dataset SEEG (`emissoes_gases`), colunas de ano com rótulo **inteiro** (`1970`…`2021`).

> Marcação de aula: 🟢 Aula 01 · 🔵 Aula 02 · 🟣 Aula 03 · 🟠 Aula 04

---

## 1. `loc` vs `iloc` 🟢

| | Seleciona por | Fatia final | Aceita máscara booleana |
|---|---|---|---|
| **`loc`** | **rótulo** (nome/valor do índice) | **inclusiva** | ✅ sim |
| **`iloc`** | **posição** inteira | **exclusiva** | ❌ não (só array de bool) |

```python
df.loc[10, 'Estado']            # rótulo de índice 10, coluna 'Estado'
df.loc[:, 1970:2021]            # colunas 1970 ATÉ 2021 (inclui 2021)
df.loc[df['Estado'] == 'PA', 2021]        # máscara + coluna, numa tacada
df.loc[mascara, ['Estado', 2021]]         # máscara + lista de colunas

df.iloc[0]                      # 1ª linha (posição)
df.iloc[0:5, 8]                 # linhas 0-4 (NÃO inclui 5), coluna de posição 8
df.iloc[-1]                     # última linha
```

**A confusão clássica:** se o índice for `0,1,2…`, rótulo e posição coincidem e os dois parecem iguais. Após um filtro, o índice fica furado (`0, 5, 23…`) e aí `loc[5]` ≠ `iloc[5]`.

```python
sul = df[df['Estado'] == 'RS']
sul.loc[23]     # linha cujo RÓTULO é 23
sul.iloc[0]     # PRIMEIRA linha do filtrado (seja qual for o rótulo)
```

**Regra:** `iloc` só quando você quer "as N primeiras/últimas". No resto, `loc`.

**Atalhos:**
```python
df.at[10, 'Estado']       # loc para 1 célula — mais rápido
df.iat[0, 8]              # iloc para 1 célula
```

---

## 2. Filtros booleanos 🟢

```python
df[df['Estado'] == 'PA']                          # igualdade
df[df['Estado'].isin(['PR', 'RS', 'SC'])]         # vários valores
df[~df['Estado'].isin(['PR', 'RS'])]              # NEGAÇÃO com ~
df[df[2021].between(1000, 5000)]                  # intervalo (inclusivo)
df[df['Estado'].isna()]                           # nulos
df[df['Nível 2'].str.contains('Química', na=False)]   # texto
```

**Combinando condições:**

| Lógica | Pandas | ❌ Nunca |
|---|---|---|
| E | `&` | `and` |
| OU | `\|` | `or` |
| NÃO | `~` | `not` |

```python
df[(df['Nível 1 - Setor'] == 'Agropecuária') & (df['Estado'] == 'PA')]
```

**Parênteses são obrigatórios.** `&` tem precedência maior que `==` — sem eles o Python lê tudo errado e quebra.

**`and`/`or` dão `ValueError: The truth value of a Series is ambiguous`** — eles comparam um valor só, não 95 mil linhas.

**`query()`** — alternativa mais legível, sem repetir o nome do DataFrame:
```python
df.query("Estado == 'PA' and `Nível 1 - Setor` == 'Agropecuária'")
df.query("Estado in ['PR','RS','SC']")
df.query("Estado == @uf")        # @ referencia variável Python
```
Nome de coluna com espaço/acento → **crase**. Dentro do `query`, `and`/`or` são permitidos (é outra sintaxe).

---

## 3. `groupby` 🔵

Modelo mental: **dividir → aplicar → combinar**.

```python
df.groupby('Estado')[2021].sum()                    # 1 chave, 1 coluna
df.groupby(['Estado', 'Nível 1 - Setor'])[2021].sum()   # 2 chaves → MultiIndex
df.groupby('Estado')[[2020, 2021]].mean()           # várias colunas
df.groupby('Estado').size()                         # nº de linhas por grupo
df.groupby('Estado')[2021].count()                  # nº de NÃO-nulos
```

**Parâmetros que evitam dor de cabeça:**

```python
df.groupby('Estado', as_index=False)[2021].sum()   # chave vira COLUNA, não índice
df.groupby('Estado', dropna=False)[2021].sum()     # inclui grupo NaN (padrão: descarta!)
df.groupby('Estado', sort=False)[2021].sum()       # não ordena — mais rápido
df.groupby('Estado', observed=True)                # só categorias presentes (Categorical)
```

⚠️ **`dropna=True` é o padrão** — linhas com chave nula somem silenciosamente do resultado. No SEEG são 5.896 linhas.

**Navegando os grupos:**
```python
g = df.groupby('Estado')
g.groups.keys()          # nomes dos grupos
g.get_group('PA')        # o DataFrame de um grupo
g.first() / g.last() / g.nth(0)
```

---

## 4. `agg` — múltiplas agregações 🔵

```python
# 1 coluna, várias funções
df.groupby('Estado')[2021].agg(['sum', 'mean', 'max', 'count'])

# colunas diferentes, funções diferentes
df.groupby('Estado').agg({2020: 'sum', 2021: ['sum', 'max']})

# NOMEADO — melhor forma: já sai com nome limpo, sem MultiIndex nas colunas
df.groupby('Estado').agg(
    total_2021=(2021, 'sum'),
    media_2021=(2021, 'mean'),
    maior=(2021, 'max'),
    n_linhas=(2021, 'size'),
)

# função própria
df.groupby('Estado')[2021].agg(lambda s: s.max() - s.min())
```

Funções prontas: `sum` `mean` `median` `min` `max` `std` `var` `count` `size` `nunique` `first` `last` `prod` `any` `all`

⚠️ `count` ignora NaN; `size` conta tudo.

---

## 5. `transform` vs `agg` vs `apply` 🔵

| | Retorna | Shape | Use para |
|---|---|---|---|
| **`agg`** | 1 valor por grupo | **reduz** (N linhas → 1 por grupo) | Totais, resumo |
| **`transform`** | 1 valor por **linha** | **mantém** (mesmo shape da entrada) | Devolver o resultado do grupo para cada linha |
| **`apply`** | qualquer coisa | livre | Quando os outros dois não dão conta |

```python
df.groupby('Estado')[2021].agg('sum')        # 27 linhas (uma por estado)
df.groupby('Estado')[2021].transform('sum')  # 94.748 linhas (o total do estado repetido)
```

**O caso em que só `transform` resolve** — criar coluna alinhada ao DataFrame original:

```python
df['total_uf']  = df.groupby('Estado')[2021].transform('sum')
df['pct_da_uf'] = df[2021] / df['total_uf'] * 100        # % que a linha representa na UF
df['acima_media'] = df[2021] > df.groupby('Estado')[2021].transform('mean')
```

Com `agg` isso exigiria agregar + `merge` de volta. `transform` faz em 1 linha.

**`apply`** é o último recurso — é o mais lento porque roda Python puro por grupo:
```python
df.groupby('Estado').apply(lambda g: g.nlargest(3, 2021), include_groups=False)   # top 3 de cada UF
```
⚠️ Sem `include_groups=False` o pandas 2.2+ emite `FutureWarning` — a coluna de agrupamento deixará de ser passada para a função.

**Ordem de escolha:** `agg` → `transform` → `apply`. Só desça um nível quando o de cima não resolver.

---

## 6. `MultiIndex` 🟣

Nasce sozinho quando você agrupa por 2+ chaves.

```python
mi = df.groupby(['Estado', 'Nível 1 - Setor'])[2021].sum()
```

**Navegar:**
```python
mi['PA']                       # nível 0
mi['PA', 'Agropecuária']       # os dois níveis
mi.loc['PA']                   # idem via loc
mi.loc[('PA', 'Energia')]      # tupla = coordenada completa
mi.xs('Energia', level=1)      # fatiar por um nível interno ← o mais útil
mi.loc[(slice(None), 'Energia')]        # equivalente com slice, em SERIES
```

⚠️ A forma com `, :` (`df.loc[(slice(None), 'Energia'), :]`) só vale para **DataFrame**. Em Series dá `IndexingError`. `xs()` funciona nos dois — prefira ele.

**Achatar (o que você vai querer 90% das vezes):**
```python
mi.reset_index()                    # níveis viram colunas → DataFrame normal
mi.reset_index(level=0)             # só o nível 0
mi.droplevel(1)                     # descarta um nível
mi.unstack()                        # nível do índice vira COLUNA (pivot)
mi.unstack().stack()                # volta
```

**Achatar MultiIndex de COLUNAS** (sobra do `agg` com lista de funções):
```python
df.columns = ['_'.join(map(str, c)).strip('_') for c in df.columns]
```

**Inspecionar / ordenar:**
```python
mi.index.names           # nomes dos níveis
mi.index.levels          # valores de cada nível
mi.sort_index()          # ORDENE antes de fatiar
```

⚠️ Fatiar MultiIndex desordenado dá `UnsortedIndexError` ou fica lento. `sort_index()` primeiro.

---

## 7. `merge` / `join` / `concat` 🟠

| | Junta por | Direção | Quando usar |
|---|---|---|---|
| **`merge`** | **coluna** (ou índice) | lado a lado | Padrão. É o JOIN do SQL |
| **`join`** | **índice** (padrão) | lado a lado | Atalho quando a chave já é índice |
| **`concat`** | posição/rótulo | empilha | Colar DataFrames de mesmo formato |

### merge

```python
pd.merge(esq, dir, on='Estado', how='inner')
pd.merge(esq, dir, left_on='uf', right_on='sigla', how='left')   # nomes diferentes
pd.merge(esq, dir, on=['Estado', 'Ano'])                          # chave composta
esq.merge(dir, on='Estado')                                       # forma encadeada
```

**Tipos de `how`:**

| `how` | Mantém | Risco |
|---|---|---|
| `inner` *(padrão)* | só chaves nos DOIS | **perde linhas silenciosamente** |
| `left` | todas da esquerda | gera NaN onde não casou |
| `right` | todas da direita | idem |
| `outer` | todas de ambos | gera NaN dos dois lados |
| `cross` | produto cartesiano | explode: N × M linhas |

### ⚠️ As duas armadilhas do merge

**1. Perder linhas.** `inner` é o padrão e descarta o que não casa — sem aviso.
```python
print(esq.shape, dir.shape)
r = pd.merge(esq, dir, on='Estado', how='left', indicator=True)
print(r['_merge'].value_counts())    # left_only = não encontrou par
```

**2. Duplicar linhas.** Se a chave se repetir do lado direito, cada linha da esquerda vira N.
```python
dir['Estado'].duplicated().any()     # confira ANTES

pd.merge(esq, dir, on='Estado', validate='one_to_one')    # levanta erro se violar
# opções: 'one_to_one' | 'one_to_many' | 'many_to_one' | 'many_to_many'
```

**`validate=` é a melhor defesa** — falha alto em vez de entregar número errado.

**Colunas de mesmo nome** ganham sufixo `_x` / `_y`. Renomeie:
```python
pd.merge(esq, dir, on='Estado', suffixes=('_2020', '_2021'))
```

### join
```python
esq.join(dir, how='left')                 # ambos pelo índice
esq.join(dir, on='Estado')                # coluna da esq × índice da dir
esq.join([df2, df3])                      # vários de uma vez
```

### concat
```python
pd.concat([df1, df2])                              # empilha LINHAS (axis=0)
pd.concat([df1, df2], ignore_index=True)           # reindexa 0..n ← quase sempre quer isso
pd.concat([df1, df2], axis=1)                      # lado a lado, alinhando pelo ÍNDICE
pd.concat([df1, df2], keys=['2020', '2021'])       # cria MultiIndex identificando a origem
```

⚠️ `axis=1` alinha pelo **índice**, não pela ordem das linhas. Índices diferentes → NaN.

---

## 8. Armadilhas gerais

### `SettingWithCopyWarning` 🟢
Filtrar pode devolver uma *view*, não uma cópia. Alterar depois é ambíguo.
```python
sub = df[df['Estado'] == 'PA'].copy()    # ← .copy() se for MEXER depois
```
É **aviso**, não erro: o código roda e a alteração pode não ir para lugar nenhum.

### Espaço invisível em texto 🟢
```python
for v in df['Nível 1 - Setor'].unique():
    print(repr(v))            # 'Resíduos ' ← só repr() denuncia
df['col'] = df['col'].str.strip()
```
Filtro errado retorna **0 linhas, sem erro**.

### `'NA'` virando NaN na leitura 🟢
`read_csv`/`read_excel` convertem `'NA'`, `'N/A'`, `'NULL'`, `'None'`, `'nan'` em `NaN` por padrão.
```python
pd.read_excel(arq, keep_default_na=False)     # desliga
df['Estado'].nunique()      # ignora NaN → 27 UFs
len(df['Estado'].unique())  # CONTA o NaN → 28 ✗
```

### Célula de notebook não é idempotente 🟢
```python
df = df.drop(columns='X')    # 2ª execução → KeyError
```
Reatribuir em cima da própria variável quebra na reexecução. Valide com `.shape` antes/depois.

### Rótulo de coluna numérico 🟢
Anos vindos do Excel são `int`, não `str`.
```python
df.loc[m, 2021]     # ✅
df.loc[m, '2021']   # ❌ KeyError
```

---

## 9. Validação — rode sempre

```python
df.shape                    # antes e depois de todo filtro/merge
df.info()                   # tipos + contagem de não-nulos
df.describe()               # estatísticas das numéricas
df.isna().sum()             # nulos por coluna
df['col'].value_counts(dropna=False)     # distribuição, incluindo NaN
df.duplicated().sum()       # linhas duplicadas
df.index.is_unique          # índice tem repetido?
```

**Checagem de soma após agrupar** — o total tem que bater:
```python
# ❌ FALHA se a coluna de agrupamento tiver NaN: groupby descarta esses grupos
assert df.groupby('Estado')[2021].sum().sum() == df[2021].sum()

# ✅ dropna=False mantém o grupo NaN e o total fecha
assert df.groupby('Estado', dropna=False)[2021].sum().sum() == df[2021].sum()
```
Se a 1ª versão falhar e a 2ª passar, você acabou de medir exatamente quanto os nulos representam.

⚠️ No SEEG esse `sum()` **não** representa emissão real: a planilha traz o mesmo gás em várias métricas (`CO2e GWP-AR2/AR4/AR5/AR6`). Somar tudo conta o mesmo gás 4×. Fixe uma métrica antes de totalizar.
