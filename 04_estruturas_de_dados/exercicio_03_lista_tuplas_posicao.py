"""Exercício 3 — Gera uma lista de tuplas (posição, nome) a partir de uma lista de nomes."""

lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo']

# enumerate retorna pares (índice, valor) que são convertidos em tuplas na nova lista
lista_com_posicao = [(i, nome) for i, nome in enumerate(lista)]

print(lista_com_posicao)
