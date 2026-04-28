"""Exercício 7 — Cria lista de tuplas (rótulo, glicose) classificando cada valor de glicemia."""

glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]

# Por que o ternário funciona encadeado?
# Python avalia da esquerda para a direita: testa <= 70 primeiro, depois <= 99, depois <= 125.
# A primeira condição verdadeira vence — os limites não precisam ser cumulativos (ex: g > 70 and g <= 99).
rotulos_glicemia = [
    (
        'Hipoglicemia' if g <= 70 else
        'Normal'       if g <= 99 else
        'Alterada'     if g <= 125 else
        'Diabetes',
        g
    )
    for g in glicemia
]

for rotulo, valor in rotulos_glicemia:
    print(f'{valor:>3} -> {rotulo}')
