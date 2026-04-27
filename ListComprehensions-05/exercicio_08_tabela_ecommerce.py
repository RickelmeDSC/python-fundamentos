"""Exercício 8 — Monta tabela de vendas com cabeçalho e total (quantidade × preço) usando list comprehension."""

ids        = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
quantidade = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
preco      = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]

# cabeçalho inserido como primeira tupla; zip agrupa os três iteráveis em paralelo
tabela = [('id', 'quantidade', 'preco', 'total')] + [
    (i, q, p, q * p) for i, q, p in zip(ids, quantidade, preco)
]

for linha in tabela:
    print(linha)
