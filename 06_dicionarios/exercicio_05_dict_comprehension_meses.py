"""Exercício 5 — Dict comprehension que mapeia meses às suas despesas usando zip()."""

meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]

# zip() emparelha cada mês com sua despesa; dict comprehension monta o dicionário
despesas_por_mes = {mes: valor for mes, valor in zip(meses, despesa)}

print(despesas_por_mes)
