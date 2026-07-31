# 📋 Cheatsheet — Dicionários

Referência rápida baseada nos exercícios 05, 09 e 10.

## Básico

```python
d = {'Jan': 860, 'Fev': 490}
d['Jan']            # acesso — KeyError se não existir
d.get('Mar', 0)     # acesso com padrão — sem erro
d['Mar'] = 1010     # inserir/atualizar
'Jan' in d          # existe a chave?
```

⚠️ Chaves são **case-sensitive**: `'Carol' != 'carol'`.

## Iterar

```python
for chave in d:                  # só chaves
for valor in d.values():         # só valores
for chave, valor in d.items():   # pares — o mais usado
```

## Dict comprehension

```python
{chave_expr: valor_expr  for item in iteravel  if condicao}
```

```python
# duas listas → dicionário (ex. 05)
despesas_por_mes = {mes: valor for mes, valor in zip(meses, despesa)}

# transformar um dict existente (ex. 10) — .items() entrega os pares
dict_soma = {estado: sum(valores) for estado, valores in dict_listas.items()}
```

## Padrão agrupar → reduzir (ex. 09 e 10)

```python
estados_unicos = set(f[0] for f in funcionarios)   # set() remove duplicatas

# passo 1: agrupar (inspecionável — facilita depurar)
dict_listas = {uf: [f[1] for f in funcionarios if f[0] == uf] for uf in estados_unicos}

# passo 2: reduzir
dict_soma = {uf: sum(vals) for uf, vals in dict_listas.items()}
```

Contagem é o mesmo padrão com `len()` no lugar de `sum()`.

## Pegadinhas

- `set()` no loop externo é obrigatório — sem ele, chaves repetidas refazem o mesmo trabalho.
- `zip()` para no menor iterável, silenciosamente.
- `d[chave]` inexistente → `KeyError`. Use `.get()` ou `try/except` (ver módulo 07).

## Conexão com Pandas

Este padrão agrupar→reduzir é **exatamente** o `groupby`:

```python
{uf: sum(...) for uf in set(...)}       # ← o que você fez na mão
df.groupby('estado')['n'].sum()          # ← a mesma coisa em 1 linha
```

Entender a versão manual é o que faz o `groupby` deixar de ser mágica.
