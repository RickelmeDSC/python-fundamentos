"""Exercício 4 — List comprehension que filtra apenas o valor numérico das tuplas do tipo 'Apartamento'."""

aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 2500)]

# extrai somente o valor (índice 1) quando o primeiro elemento for 'Apartamento'
valores_apartamento = [tupla[1] for tupla in aluguel if tupla[0] == 'Apartamento']

print(valores_apartamento)
