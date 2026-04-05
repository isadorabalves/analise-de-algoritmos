"""
Análise de recorrências utilizando o Teorema Mestre.

O Teorema Mestre é utilizado para determinar a complexidade de algoritmos
recursivos da forma:

    T(n) = aT(n/b) + f(n)

Onde:
- a: número de subproblemas
- b: fator de divisão do problema
- f(n): custo adicional fora da recursão

A análise consiste em comparar f(n) com n^(log_b(a)) para determinar
o comportamento assintótico da recorrência.
"""

def analisar_recorrencias():
    """
    Mostra os resultados das recorrências propostas.
    """
    print("1) T(n) = 2T(n/4) + √n")
    print("Resultado: Θ(√n log n)\n")

    print("2) T(n) = 2T(n/4) + n")
    print("Resultado: Θ(n)\n")

    print("3) T(n) = 16T(n/4) + n²")
    print("Resultado: Θ(n² log n)")


def main():
    """
    Executa a análise das recorrências.
    """
    analisar_recorrencias()


if __name__ == "__main__":
    main()