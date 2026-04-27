"""Exercício 2 — Gera uma lista com o terceiro elemento de cada tupla em uma lista de tuplas."""

lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 85)]

# acessa o índice 2 de cada tupla (terceiro elemento) e armazena numa nova lista
terceiros_elementos = [tupla[2] for tupla in lista_de_tuplas]

print(terceiros_elementos)
