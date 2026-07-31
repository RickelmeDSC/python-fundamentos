# 📋 Cheatsheet — Exceções

Referência rápida baseada nos exercícios 11–14 e desafios 01–03.

## Estrutura completa

```python
try:
    resultado = a / b            # código que pode falhar
except ValueError as e:          # trata erro ESPECÍFICO
    print(f"Erro do tipo {type(e).__name__}: {e}")
except ZeroDivisionError:
    print("divisão por zero")
finally:
    print("roda SEMPRE — com ou sem erro")   # fechar arquivo/conexão
```

- **Um `except` por tipo de erro** — genérico (`except Exception`) esconde qual erro ocorreu.
- `as e` só quando a mensagem usa os detalhes; mensagem fixa dispensa.
- `type(e).__name__` → o nome do erro (`'ValueError'`).
- `finally` roda **antes** de o `return` chegar ao chamador.

## Erros que você já tratou

| Erro | Quando acontece |
|---|---|
| `ValueError` | `float('abc')` — tipo certo, valor inválido |
| `ZeroDivisionError` | `a / 0` |
| `KeyError` | `d['chave_inexistente']` |
| `TypeError` | `4 + 'A'` — tipos incompatíveis |
| `IndexError` | posição fora da lista (ou lançado manualmente) |

## `raise` — lançar de propósito

```python
if len(lista1) != len(lista2):
    raise ValueError(f"Tamanhos diferentes: {len(lista1)} e {len(lista2)}.")
```

**Onde tratar?** Regra dos desafios:
- Violação de **contrato** (entrada inválida) → `raise` **fora** do try; quem chamou decide o que fazer.
- Problema **interno** do processamento → `try/except` **dentro** da função.

## Padrões dos desafios

```python
# Tudo-ou-nada (desafio 01): valide TUDO antes de calcular —
# senão um erro no meio deixa resultado parcial ambíguo
for teste in testes:
    for alt in teste:
        if alt not in ['A', 'B', 'C', 'D']:
            raise ValueError(f"Alternativa {alt} inválida")
notas = [...]   # só calcula depois de validar

# Falhe na primeira ocorrência (desafio 02) — em pipeline,
# corrige-se um problema por vez
if ',' in palavra or '.' in palavra:
    raise ValueError(f'Pontuação na palavra "{palavra}".')

# Valide o que o zip() esconderia (desafio 03) —
# zip trunca silenciosamente no menor
if len(lista_1) != len(lista_2):
    raise ValueError("tamanhos diferentes")
```

## Conexão com dados

Validação antes do processamento é o **teste de qualidade do pipeline**: conferir shape, tipos e nulos antes de calcular é a versão Pandas do `raise` antes do loop. `errors='coerce'`/`'ignore'` do `pd.to_numeric` são o try/except embutido do pandas.
