"""
Dever 12 — Algoritmo de Kruskal

Objetivo:
Modificar o algoritmo de Kruskal para encontrar
a árvore geradora máxima, ou seja, o caminho mais caro
sem formar ciclos.

"""

import time


class Grafo:
    """
    Representa um grafo ponderado não direcionado.

    O grafo utiliza uma lista de arestas, em que cada aresta
    possui origem, destino e peso.
    """

    def __init__(self, vertices):
        """
        Inicializa o grafo.

        Args:
            vertices (int): quantidade de vértices do grafo.
        """
        self.vertices = vertices
        self.arestas = []

    def adicionar_aresta(self, origem, destino, peso):
        """
        Adiciona uma aresta ao grafo.

        Args:
            origem (int): vértice de origem.
            destino (int): vértice de destino.
            peso (int): custo da aresta.
        """
        self.arestas.append([origem, destino, peso])

    def buscar_raiz(self, pai, vertice):
        """
        Busca a raiz de um vértice usando compressão de caminho.

        Args:
            pai (list): lista de representantes dos conjuntos.
            vertice (int): vértice consultado.

        Returns:
            int: raiz do conjunto ao qual o vértice pertence.
        """
        if pai[vertice] == vertice:
            return vertice

        pai[vertice] = self.buscar_raiz(pai, pai[vertice])
        return pai[vertice]

    def unir_conjuntos(self, pai, rank, raiz_x, raiz_y):
        """
        Une dois conjuntos utilizando união por rank.

        Args:
            pai (list): lista de representantes dos conjuntos.
            rank (list): lista de ranks dos conjuntos.
            raiz_x (int): raiz do primeiro conjunto.
            raiz_y (int): raiz do segundo conjunto.
        """
        if rank[raiz_x] < rank[raiz_y]:
            pai[raiz_x] = raiz_y
        elif rank[raiz_x] > rank[raiz_y]:
            pai[raiz_y] = raiz_x
        else:
            pai[raiz_y] = raiz_x
            rank[raiz_x] += 1

    def executar_kruskal_maximo(self):
        """
        Executa o algoritmo de Kruskal para árvore geradora máxima.

        Diferente da versão tradicional, que ordena as arestas
        do menor para o maior peso, esta versão ordena do maior
        para o menor peso, buscando o maior custo possível
        sem formar ciclos.

        Returns:
            tuple: lista de arestas escolhidas e custo total.
        """
        resultado = []
        indice_aresta = 0
        total_arestas = 0
        custo_total = 0

        arestas_ordenadas = sorted(
            self.arestas,
            key=lambda item: item[2],
            reverse=True
        )

        pai = []
        rank = []

        for vertice in range(self.vertices):
            pai.append(vertice)
            rank.append(0)

        while total_arestas < self.vertices - 1:
            origem, destino, peso = arestas_ordenadas[indice_aresta]
            indice_aresta += 1

            raiz_origem = self.buscar_raiz(pai, origem)
            raiz_destino = self.buscar_raiz(pai, destino)

            if raiz_origem != raiz_destino:
                resultado.append([origem, destino, peso])
                custo_total += peso
                total_arestas += 1

                self.unir_conjuntos(
                    pai,
                    rank,
                    raiz_origem,
                    raiz_destino
                )

        return resultado, custo_total


def criar_grafo_teste():
    """
    Cria o grafo utilizado no caso de teste da atividade.

    Returns:
        Grafo: grafo preenchido com as arestas.
    """
    grafo = Grafo(8)

    grafo.adicionar_aresta(4, 7, 1)
    grafo.adicionar_aresta(5, 6, 2)
    grafo.adicionar_aresta(4, 5, 3)
    grafo.adicionar_aresta(6, 7, 4)
    grafo.adicionar_aresta(0, 1, 5)
    grafo.adicionar_aresta(3, 7, 6)
    grafo.adicionar_aresta(2, 5, 7)
    grafo.adicionar_aresta(2, 6, 8)
    grafo.adicionar_aresta(1, 2, 9)
    grafo.adicionar_aresta(1, 6, 10)
    grafo.adicionar_aresta(1, 5, 11)
    grafo.adicionar_aresta(1, 7, 13)
    grafo.adicionar_aresta(1, 4, 14)
    grafo.adicionar_aresta(0, 4, 15)
    grafo.adicionar_aresta(0, 3, 16)
    grafo.adicionar_aresta(3, 6, 17)
    grafo.adicionar_aresta(0, 7, 18)

    return grafo


def imprimir_resultado(arestas, custo_total, tempo_execucao):
    """
    Exibe o resultado da árvore geradora máxima no terminal.

    Args:
        arestas (list): arestas escolhidas pelo algoritmo.
        custo_total (int): custo total da árvore geradora.
        tempo_execucao (float): tempo gasto na execução.
    """
    print("=" * 60)
    print("RESULTADO DO ALGORITMO DE KRUSKAL")
    print("ÁRVORE GERADORA MÁXIMA")
    print("=" * 60)

    print("\nRotas escolhidas para a rede:")

    for origem, destino, peso in arestas:
        print(
            f"Rota da cidade {origem} para a cidade {destino} "
            f"| Custo: {peso}"
        )

    print("\n" + "=" * 60)
    print(f"Custo total da árvore geradora máxima: {custo_total}")
    print(f"Tempo de execução: {tempo_execucao:.4f} milissegundos")
    print("=" * 60)


def main():
    """
    Executa o programa principal.
    """
    grafo = criar_grafo_teste()

    inicio = time.perf_counter()

    arestas, custo_total = grafo.executar_kruskal_maximo()

    fim = time.perf_counter()
    tempo_execucao = (fim - inicio) * 1000

    imprimir_resultado(
        arestas,
        custo_total,
        tempo_execucao
    )


if __name__ == "__main__":
    main()