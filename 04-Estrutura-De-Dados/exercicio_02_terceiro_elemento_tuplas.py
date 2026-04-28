"""Exercício 2 — Gera uma lista com o terceiro elemento de cada tupla em uma lista de tuplas."""

lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 85)]

# Por que índice 2 para o terceiro elemento?
# Python usa índice base 0: posição 0 = primeiro, 1 = segundo, 2 = terceiro.
# Por que list comprehension em vez de for + append?
# A comprehension é uma expressão que constrói e retorna a lista em uma linha — mais legível quando a transformação é simples.
terceiros_elementos = [tupla[2] for tupla in lista_de_tuplas]

print(terceiros_elementos)
