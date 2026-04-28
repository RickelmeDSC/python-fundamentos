"""Exercício 1 — Soma dos elementos de cada sublista contida em uma lista de listas."""

lista_de_listas = [[4, 6, 5, 9], [1, 0, 7, 2], [3, 4, 1, 8]]

# Por que sum() em vez de um loop acumulando manualmente?
# sum() aceita qualquer iterável e comunica a intenção diretamente — sem variável auxiliar.
for sublista in lista_de_listas:
    print(sum(sublista))
