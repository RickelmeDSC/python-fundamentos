"""Exercício 14 — Agrupa duas listas em tuplas (val1, val2, soma) com tratamento de exceção."""


def agrupa_listas(lista1, lista2):
    # Por que raise IndexError fora do try?
    # A função lança o erro intencionalmente — é uma violação de contrato (tamanhos diferentes).
    # Quem chama a função é responsável por decidir o que fazer com esse erro.
    if len(lista1) != len(lista2):
        raise IndexError('A quantidade de elementos em cada lista é diferente.')
    try:
        resultado = [(lista1[i], lista2[i], lista1[i] + lista2[i]) for i in range(len(lista1))]
        return resultado
    except TypeError as e:
        # TypeError é um erro interno do processamento (soma de tipos incompatíveis).
        # A função o trata aqui porque é um problema dela, não de quem a chamou.
        print(f"Erro do tipo {type(e).__name__}: {e}")


# Teste sem erro
lista1 = [4, 6, 7, 9, 10]
lista2 = [-4, 6, 8, 7, 9]
print(agrupa_listas(lista1, lista2))

# Teste com listas de tamanhos diferentes
lista1 = [4, 6, 7, 9, 10, 4]
lista2 = [-4, 6, 8, 7, 9]
try:
    print(agrupa_listas(lista1, lista2))
except IndexError as e:
    print(f"Erro do tipo {type(e).__name__}: {e}")

# Teste com valores incoerentes
lista1 = [4, 6, 7, 9, 'A']
lista2 = [-4, 'E', 8, 7, 9]
print(agrupa_listas(lista1, lista2))
