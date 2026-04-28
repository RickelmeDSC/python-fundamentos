"""Exercício 15 — Contabiliza pontuações de estudantes com validação de alternativas via raise."""

gabarito = ['D', 'A', 'B', 'C', 'A']

testes_sem_ex  = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]
testes_com_ex  = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]


def calcular_notas(gabarito, testes):
    # Por que validar TUDO antes de calcular?
    # Se calcularmos na ordem e lançarmos erro no meio, teríamos notas parciais — comportamento ambíguo.
    # Validar primeiro garante comportamento tudo-ou-nada: ou todas as notas saem, ou nenhuma.
    for teste in testes:
        for alternativa in teste:
            if alternativa not in ['A', 'B', 'C', 'D']:
                raise ValueError(f"A alternativa {alternativa} não é uma opção de alternativa válida")

    # zip() emparelha a resposta do estudante com a do gabarito na mesma posição
    notas = [sum(1 for resp, gab in zip(teste, gabarito) if resp == gab) for teste in testes]
    return notas


# Teste sem exceção
try:
    print(calcular_notas(gabarito, testes_sem_ex))
except ValueError as e:
    print(f"Erro do tipo {type(e).__name__}: {e}")

# Teste com exceção
try:
    print(calcular_notas(gabarito, testes_com_ex))
except ValueError as e:
    print(f"Erro do tipo {type(e).__name__}: {e}")
