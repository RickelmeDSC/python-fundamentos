"""Exercício 1 — Soma dos elementos de cada sublista contida em uma lista de listas."""

lista_de_listas = [[4, 6, 5, 9], [1, 0, 7, 2], [3, 4, 1, 8]]

# percorre cada sublista e imprime a soma dos seus elementos
for sublista in lista_de_listas:
    print(sum(sublista))
