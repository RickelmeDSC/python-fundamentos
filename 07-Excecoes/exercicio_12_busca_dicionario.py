"""Exercício 12 — Busca em dicionário com tratamento de KeyError."""

idades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}

# Atenção: chaves de dicionário são case-sensitive — 'carol' e 'Carol' são chaves diferentes.
chave = input("Digite um nome para buscar: ")

try:
    resultado = idades[chave]
    print(resultado)
except KeyError:
    # Por que não usar 'as e' aqui? A mensagem é fixa — não precisamos dos detalhes do erro.
    # Capturar em variável seria código desnecessário.
    print("Nome não encontrado")
