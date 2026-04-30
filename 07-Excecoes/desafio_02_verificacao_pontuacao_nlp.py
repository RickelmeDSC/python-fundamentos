"""Desafio 02 — Verifica se uma lista de palavras contém pontuações não tratadas (contexto NLP)."""

lista_tratada = [
    'Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa', 'versátil',
    'e', 'fácil', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos', 'desde',
    'análise', 'de', 'dados', 'até', 'inteligência', 'artificial',
]

lista_nao_tratada = [
    'Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa,', 'versátil',
    'e', 'fácil,', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos,', 'desde',
    'análise', 'de', 'dados', 'até', 'inteligência', 'artificial!',
]


def verificar_pontuacao(lista_palavras):
    for palavra in lista_palavras:
        # Por que 'or' em vez de verificar cada símbolo separadamente?
        # 'or' faz curto-circuito: assim que uma condição é True, Python para de avaliar as demais.
        # Também é mais legível do que quatro ifs aninhados.
        if ',' in palavra or '.' in palavra or '!' in palavra or '?' in palavra:
            # Por que lançar na PRIMEIRA ocorrência e não listar todas?
            # Em pipelines reais, você corrige um problema de cada vez — reportar o primeiro
            # já permite ao desenvolvedor identificar e revisar o pré-processamento.
            raise ValueError(f'O texto apresenta pontuações na palavra "{palavra}".')


# Teste com lista tratada
try:
    verificar_pontuacao(lista_tratada)
    print("Nenhuma pontuação encontrada — texto pronto para processamento.")
except ValueError as e:
    print(f"Erro do tipo {type(e).__name__}: {e}")

# Teste com lista não tratada
try:
    verificar_pontuacao(lista_nao_tratada)
    print("Nenhuma pontuação encontrada — texto pronto para processamento.")
except ValueError as e:
    print(f"Erro do tipo {type(e).__name__}: {e}")


# Conexão com dados/IA: em NLP, o pré-processamento (remover pontuação, normalizar texto, tokenizar)
#  é obrigatório antes de qualquer análise ou modelo. Essa função seria o teste de qualidade que garante
#  que o texto já passou pelo tratamento antes de entrar no pipeline.