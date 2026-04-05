"""
Implementação do Merge Sort.

O Merge Sort é um algoritmo de ordenação baseado na estratégia
"dividir para conquistar".

Funcionamento:
1. Divide a lista em duas partes menores;
2. Aplica o próprio algoritmo (recursivamente) em cada parte;
3. Junta (merge) as partes já ordenadas, formando uma nova lista ordenada.

Características:
- Sempre divide a lista até chegar em listas com apenas 1 elemento;
- Depois combina essas listas de forma ordenada;
- Não depende da ordem inicial dos dados.

Complexidade:
- Tempo: O(n log n) em todos os casos;
- Espaço: O(n), pois utiliza listas auxiliares.
"""


def merge_sort(lista):
    """
    Ordena uma lista usando o algoritmo Merge Sort.

    O algoritmo divide a lista recursivamente até obter sublistas
    com apenas um elemento, e então realiza a junção ordenada dessas partes.

    Args:
        lista (list): Lista de números a ser ordenada.

    Returns:
        list: Nova lista ordenada.
    """
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2

    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])

    resultado = []
    i = 0
    j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    while i < len(esquerda):
        resultado.append(esquerda[i])
        i += 1

    while j < len(direita):
        resultado.append(direita[j])
        j += 1

    return resultado


def main():
    """
    Permite ao usuário inserir os valores da lista e executar o Merge Sort.
    """
    entrada = input("Digite números separados por espaço: ")

    lista = list(map(int, entrada.split()))

    print("\nLista original:", lista)
    print("Lista ordenada:", merge_sort(lista))

    print("\nComplexidade:")
    print("Tempo: O(n log n)")
    print("Espaço: O(n)")


if __name__ == "__main__":
    main()