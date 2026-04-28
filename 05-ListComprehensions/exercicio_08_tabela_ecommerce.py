"""Exercício 8 — Monta tabela de vendas com cabeçalho e total (quantidade × preço) usando list comprehension."""

# Por que 'ids' e não 'id'?
# id é uma função built-in do Python que retorna o endereço de memória de um objeto.
# Usar 'id' como variável sobrescreve essa função no escopo atual — pode causar bugs sutis.
ids        = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
quantidade = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
preco      = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]

# Por que inserir o cabeçalho como primeira tupla antes da comprehension?
# zip() só entrega valores, não sabe o nome das colunas — o cabeçalho precisa ser adicionado manualmente.
tabela = [('id', 'quantidade', 'preco', 'total')] + [
    (i, q, p, q * p) for i, q, p in zip(ids, quantidade, preco)
]

for linha in tabela:
    print(linha)
