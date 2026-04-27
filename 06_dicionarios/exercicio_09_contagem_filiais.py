"""Exercício 9 — Conta filiais por estado usando passo intermediário e dict comprehension."""

estados = [
    'SP', 'ES', 'MG', 'MG', 'SP', 'MG', 'ES', 'ES', 'ES', 'SP',
    'SP', 'MG', 'ES', 'SP', 'RJ', 'MG', 'RJ', 'SP', 'MG', 'SP',
    'ES', 'SP', 'MG',
]

# passo intermediário: lista de listas, cada uma com as ocorrências de um único estado
listas_por_estado = [[e for e in estados if e == estado] for estado in set(estados)]

# dict comprehension: chave = nome do estado, valor = quantidade de ocorrências
contagem_filiais = {lista[0]: len(lista) for lista in listas_por_estado}

print(contagem_filiais)
