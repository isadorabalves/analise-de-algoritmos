"""
Implementação da multiplicação de matrizes.

A multiplicação de matrizes consiste em combinar linhas da primeira matriz
com colunas da segunda matriz para gerar uma nova matriz.

Como funciona?
1. Cada posição da matriz resultado é calculada multiplicando os elementos
   da linha da matriz A pelos elementos da coluna da matriz B;
2. Os resultados dessas multiplicações são somados;
3. Esse processo é repetido para todas as posições da matriz final.

Requisito:
- O número de colunas da matriz A deve ser igual ao número de linhas da matriz B.

Complexidade:
- Tempo: O(n³), pois utiliza três laços de repetição aninhados;
- Espaço: O(n²), correspondente ao tamanho da matriz resultado.
"""


def multiplicar_matrizes(a, b):
    """
    Multiplica duas matrizes.

    Args:
        a (list): Primeira matriz.
        b (list): Segunda matriz.

    Returns:
        list: Matriz resultante da multiplicação.
    """
    resultado = []

    for i in range(len(a)):
        linha = []
        for j in range(len(b[0])):
            soma = 0
            for k in range(len(b)):
                soma = soma + a[i][k] * b[k][j]
            linha.append(soma)
        resultado.append(linha)

    return resultado


def ler_matriz(linhas, colunas, nome):
    """
    Lê uma matriz digitada pelo usuário.

    O usuário deve inserir os valores linha por linha, separados por espaço.

    Args:
        linhas (int): Número de linhas.
        colunas (int): Número de colunas.
        nome (str): Nome da matriz.

    Returns:
        list: Matriz preenchida.
    """
    print(f"\nDigite os valores da matriz {nome}:")

    matriz = []
    for i in range(linhas):
        linha = list(map(int, input(f"Linha {i+1}: ").split()))
        matriz.append(linha)

    return matriz


def mostrar_matriz(matriz):
    """
    Mostra a matriz linha por linha.

    Args:
        matriz (list): Matriz a ser exibida.
    """
    for linha in matriz:
        print(linha)


def main():
    """
    Permite ao usuário escolher o tamanho das matrizes e realiza a multiplicação.
    """
    linhas_a = int(input("Número de linhas da matriz A: "))
    colunas_a = int(input("Número de colunas da matriz A: "))

    linhas_b = int(input("Número de linhas da matriz B: "))
    colunas_b = int(input("Número de colunas da matriz B: "))

    if colunas_a != linhas_b:
        print("\nErro: número de colunas de A deve ser igual ao número de linhas de B.")
        return

    matriz_a = ler_matriz(linhas_a, colunas_a, "A")
    matriz_b = ler_matriz(linhas_b, colunas_b, "B")

    resultado = multiplicar_matrizes(matriz_a, matriz_b)

    print("\nResultado:")
    mostrar_matriz(resultado)

    print("\nComplexidade:")
    print("Tempo: O(n³)")
    print("Espaço: O(n²)")


if __name__ == "__main__":
    main()