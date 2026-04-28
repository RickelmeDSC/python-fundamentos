"""Exercício 13 — Converte lista para float com tratamento de exceção e cláusula finally."""


def converte_para_float(lista):
    try:
        lista_float = [float(valor) for valor in lista]
        return lista_float
    except ValueError as e:
        print(f"Erro do tipo {type(e).__name__}: {e}")
    finally:
        # Por que finally imprime antes do resultado aparecer no print externo?
        # Python avalia o valor de retorno, executa o finally, e só então entrega o valor ao chamador.
        # Por isso "Fim da execução da função" sempre aparece antes do resultado.
        # finally também roda quando há erro — por isso é usado para fechar arquivos e conexões.
        print("Fim da execução da função")


# Teste sem erro
print(converte_para_float([1, 2, 3, '4.5']))

# Teste com erro
print(converte_para_float([1, 2, 'abc', 4]))
