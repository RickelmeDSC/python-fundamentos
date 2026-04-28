"""Exercício 3 — Gera uma lista de tuplas (posição, nome) a partir de uma lista de nomes."""

lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo']

# Por que enumerate() em vez de range(len(lista))?
# enumerate() entrega o par (índice, valor) diretamente — sem precisar acessar lista[i] manualmente.
lista_com_posicao = [(i, nome) for i, nome in enumerate(lista)]

print(lista_com_posicao)
