"""Exercício 11 — Divisão entre dois números com tratamento de exceção."""

# Por que dois except separados em vez de um except Exception genérico?
# Cada erro tem uma causa diferente e merece uma mensagem diferente.
# Um except genérico esconderia qual erro realmente ocorreu.
try:
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    resultado = a / b
    print(f"Resultado: {resultado}")
except ValueError as e:
    # ValueError: float() recebeu texto que não representa um número
    print(f"Erro do tipo {type(e).__name__}: valor inválido — digite apenas números.")
except ZeroDivisionError as e:
    # ZeroDivisionError: divisão por zero é matematicamente indefinida
    print(f"Erro do tipo {type(e).__name__}: não é possível dividir por zero.")
