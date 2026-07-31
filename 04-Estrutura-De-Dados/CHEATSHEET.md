# 📋 Cheatsheet — Estruturas de Dados

Referência rápida baseada nos exercícios 01–03.

## Listas

```python
lista = [4, 6, 5, 9]
lista[0]        # primeiro (índice base 0)
lista[-1]       # último
lista[1:3]      # fatia — fim EXCLUSIVO
sum(lista)      # soma sem loop manual
len(lista)      # tamanho
```

## Listas aninhadas (lista de listas)

```python
lista_de_listas = [[4, 6, 5, 9], [1, 0, 7, 2]]

for sublista in lista_de_listas:
    print(sum(sublista))        # soma de cada sublista
```

## Tuplas

Imutáveis — servem para registros de posição fixa (nome, altura, peso).

```python
tupla = ('Pedro', 1.74, 81)
tupla[2]                        # terceiro elemento → índice 2

# extrair um campo de cada tupla
lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67)]
pesos = [t[2] for t in lista_de_tuplas]

# desempacotamento — mais legível que índices
for nome, altura, peso in lista_de_tuplas:
    print(nome, peso)
```

## `enumerate()` — índice + valor juntos

```python
lista = ['Pedro', 'Júlia', 'Otávio']

# ✅ entrega o par (índice, valor) direto
lista_com_posicao = [(i, nome) for i, nome in enumerate(lista)]

# ❌ evite: range(len(lista)) + lista[i] — mais verboso, mesmo resultado
```

## Regras que valem sempre

- Índice base 0: posição 0 = primeiro, 2 = **terceiro**.
- Fatia `a[i:j]` inclui `i`, exclui `j`.
- `sum()` aceita qualquer iterável — comunica intenção melhor que acumulador manual.

## Conexão com Pandas

| Aqui | Lá |
|---|---|
| lista de tuplas | linhas de um DataFrame |
| `t[2]` de cada tupla | `df['coluna']` |
| `enumerate()` | o índice do DataFrame |
