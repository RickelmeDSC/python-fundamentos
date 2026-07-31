# 📋 Cheatsheet — List Comprehensions

Referência rápida baseada nos exercícios 04, 06, 07 e 08.

## Anatomia

```python
[expressao  for item in iteravel  if condicao]
#  ↑ o que sai   ↑ de onde vem      ↑ filtro (opcional)
```

## Formas que você já usou

```python
# transformar
terceiros = [t[2] for t in lista_de_tuplas]

# filtrar + extrair (ex. 04)
valores = [t[1] for t in aluguel if t[0] == 'Apartamento']

# filtro com duas condições (ex. 06)
vendas_alvo = [v for v in vendas if v[0] == '2022' and v[1] > 6000]

# zip() + cálculo inline (ex. 08)
tabela = [(i, q, p, q * p) for i, q, p in zip(ids, quantidade, preco)]
```

## Ternário encadeado (ex. 07)

`if/else` na **expressão** classifica cada item; avalia da esquerda para a direita e a primeira condição verdadeira vence — os limites não precisam ser cumulativos.

```python
rotulos = [
    ('Hipoglicemia' if g <= 70 else
     'Normal'       if g <= 99 else
     'Alterada'     if g <= 125 else
     'Diabetes', g)
    for g in glicemia
]
```

**Posição importa:**
- filtro (`if` sem `else`) → vai no **fim**: `[x for x in xs if cond]`
- escolha de valor (`if/else`) → vai no **começo**: `[a if cond else b for x in xs]`

## `zip()`

```python
tabela = list(zip(ids, quantidade, preco))   # emparelha posição a posição
```

⚠️ Para **silenciosamente** no menor iterável — tamanhos diferentes não dão erro, itens extras somem. Valide `len()` antes se isso for problema.

## Pegadinhas já vividas

- `'2022' != 2022` — string e int nunca são iguais; confira o tipo antes de comparar.
- Não use `id` como variável — sobrescreve a função built-in `id()`. Use `ids`.
- Cabeçalho de tabela entra manual: `[('id', 'qtd', ...)] + [comprehension]` — o `zip()` só entrega valores.

## Conexão com Pandas

| Aqui | Lá |
|---|---|
| `[t[1] for t in xs if t[0] == 'A']` | `df.loc[df['tipo'] == 'A', 'valor']` |
| ternário encadeado | `pd.cut()` / `np.select()` |
| `q * p` no zip | `df['qtd'] * df['preco']` (vetorizado) |
