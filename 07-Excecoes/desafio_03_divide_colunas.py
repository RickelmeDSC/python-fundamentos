"""Desafio 03 — Divide duas colunas de dados experimentais com tratamento de ValueError e ZeroDivisionError."""

pressoes_ok      = [100, 120, 140, 160, 180]
temperaturas_ok  = [20, 25, 30, 35, 40]

pressoes_zero    = [60, 120, 140, 160, 180]
temperaturas_zero = [0, 25, 30, 35, 40]

pressoes_tamanho    = [100, 120, 140, 160]
temperaturas_tamanho = [20, 25, 30, 35, 40]


def divide_colunas(lista_1, lista_2):
    try:
        # Por que verificar tamanhos mesmo usando zip()?
        # zip() silenciosamente trunca para o menor iterável — sem essa verificação,
        # listas de tamanhos diferentes gerariam um resultado parcial sem nenhum aviso.
        if len(lista_1) != len(lista_2):
            raise ValueError(f"As listas têm tamanhos diferentes: {len(lista_1)} e {len(lista_2)}.")

        # ZeroDivisionError é lançado naturalmente pelo Python ao encontrar b == 0
        resultado = [a / b for a, b in zip(lista_1, lista_2)]
        return resultado

    except ValueError as e:
        print(f"Erro do tipo {type(e).__name__}: {e}")
    except ZeroDivisionError as e:
        # Por que dois except separados em vez de um except Exception?
        # Cada erro tem uma causa e mensagem diferentes — um except genérico
        # trataria ambos da mesma forma, perdendo a precisão do diagnóstico.
        print(f"Erro do tipo {type(e).__name__}: divisão por zero encontrada nos dados.")


# Teste sem exceção
print(divide_colunas(pressoes_ok, temperaturas_ok))

# Teste com ZeroDivisionError
print(divide_colunas(pressoes_zero, temperaturas_zero))

# Teste com ValueError
print(divide_colunas(pressoes_tamanho, temperaturas_tamanho))

# Conexão com dados: dividir colunas é uma das operações mais comuns em análise
#  — cálculo de taxa, razão, normalização. Quando você chegar no Pandas, fará isso com df['pressao'] / df['temperatura'],
# mas o tratamento de zeros e tamanhos incompatíveis continua sendo sua responsabilidade.