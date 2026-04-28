"""Exercício 9 — Conta filiais por estado usando passo intermediário e dict comprehension."""

estados = [
    'SP', 'ES', 'MG', 'MG', 'SP', 'MG', 'ES', 'ES', 'ES', 'SP',
    'SP', 'MG', 'ES', 'SP', 'RJ', 'MG', 'RJ', 'SP', 'MG', 'SP',
    'ES', 'SP', 'MG',
]

# Por que set(estados)? set() remove duplicatas — sem ele, o loop externo repetiria
# estados que aparecem mais de uma vez, gerando listas redundantes.
listas_por_estado = [[e for e in estados if e == estado] for estado in set(estados)]

# Por que passo intermediário em vez de contar direto?
# Separar "agrupar" de "contar" facilita depuração: dá para inspecionar listas_por_estado antes de reduzir.
contagem_filiais = {lista[0]: len(lista) for lista in listas_por_estado}

print(contagem_filiais)
