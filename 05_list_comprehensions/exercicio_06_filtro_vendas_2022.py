"""Exercício 6 — Filtra vendas do ano 2022 com valor maior que 6000 usando list comprehension."""

vendas = [
    ('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883),
    ('2023', 9859), ('2022', 5141), ('2022', 7688), ('2022', 9544),
    ('2023', 4794), ('2021', 7178), ('2022', 3030), ('2021', 7471),
    ('2022', 4226), ('2022', 8190), ('2021', 9680), ('2022', 5616),
]

# filtra tuplas onde o ano é '2022' e o valor de venda supera 6000
vendas_2022_acima_6000 = [venda for venda in vendas if venda[0] == '2022' and venda[1] > 6000]

print(vendas_2022_acima_6000)
