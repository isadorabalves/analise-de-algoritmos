"""
Implementação de um algoritmo recursivo para verificar se um array é palíndromo.

Este código foi desenvolvido como solução da atividade 3 da disciplina,
com o objetivo de analisar se os elementos de um array formam um palíndromo,
ou seja, se apresentam a mesma sequência quando lidos da esquerda para a direita
e vice-versa.

"""


def eh_palindromo(array, inicio, fim):
    """
    Função criada para verificar, recursivamente, se um array é palíndromo.

    Args:
        array (list): é a lista de elementos.
        inicio (int): refere-se ao índice inicial.
        fim (int): refere-se ao índice final.

    Returns:
        bool: True se for palíndromo, False caso não o seja.
    """
    if inicio >= fim:
        return True

    if array[inicio] != array[fim]:
        return False

    return eh_palindromo(array, inicio + 1, fim - 1)


def ler_array():
    """
    Função criada para ler um array digitado pelo usuário.

    Returns:
        list: a lista de elementos digitados.
    """
    entrada = input("Digite os elementos do array: ")

    # Criado para dividir a entrada em uma lista.
    array = entrada.split()

    return array


def main():
    """
    Função principal do programa.
    """
    array = ler_array()

    if len(array) == 0:
        print("Array vazio.")
        return

    resultado = eh_palindromo(array, 0, len(array) - 1)

    if resultado:
        print("É palíndromo")
    else:
        print("Não é palíndromo")

main()