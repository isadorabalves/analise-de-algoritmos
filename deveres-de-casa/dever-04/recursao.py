"""
Implementação de uma função recursiva para calcular F(n).

A função segue a regra:
F(n) = 2 * F(n - 1) + n²

Caso base:
F(1) = 2

O programa pede um valor de n ao usuário e mostra o resultado.
"""


def calcular_f(n):
    """
    Calcula F(n) usando recursão.

    A função chama ela mesma diminuindo o valor de n
    até chegar no caso base (n == 1).

    Args:
        n (int): número inteiro positivo

    Returns:
        int: resultado de F(n)
    """

    # caso base (quando a recursão para)
    if n == 1:
        return 2

    # chamada recursiva
    return 2 * calcular_f(n - 1) + n ** 2


# pede o valor ao usuário
n = int(input("Digite um valor para n: "))

# verifica se o valor é válido
if n < 1:
    print("Digite um valor maior ou igual a 1.")
else:
    resultado = calcular_f(n)
    print(f"F({n}) = {resultado}")

    """
    A função é recursiva porque ela chama ela mesma (calcular_f(n - 1)), diminuindo o valor de n até chegar no caso base n = 1. Quando chega em n = 1, ela para e começa a retornar os valores até chegar no resultado final.
    """