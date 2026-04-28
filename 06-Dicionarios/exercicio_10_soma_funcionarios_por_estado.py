"""Exercício 10 — Agrupa e soma colaboradores por estado a partir de lista de tuplas."""

funcionarios = [
    ('SP', 16), ('ES', 8),  ('MG', 9),  ('MG', 6),  ('SP', 10),
    ('MG', 4),  ('ES', 9),  ('ES', 7),  ('ES', 12), ('SP', 7),
    ('SP', 11), ('MG', 8),  ('ES', 8),  ('SP', 9),  ('RJ', 13),
    ('MG', 5),  ('RJ', 9),  ('SP', 12), ('MG', 10), ('SP', 7),
    ('ES', 14), ('SP', 10), ('MG', 12),
]

estados_unicos = set(f[0] for f in funcionarios)

# Por que dois dicionários separados em vez de calcular a soma direto?
# dict_listas permite inspecionar os valores agrupados antes de somá-los — útil para depurar.
dict_listas = {estado: [f[1] for f in funcionarios if f[0] == estado] for estado in estados_unicos}

# .items() retorna pares (chave, valor) — permite reutilizar dict_listas sem reler a lista original.
dict_soma = {estado: sum(valores) for estado, valores in dict_listas.items()}

print('Listas por estado:')
print(dict_listas)

print('\nSoma por estado:')
print(dict_soma)
