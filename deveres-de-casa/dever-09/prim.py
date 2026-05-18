"""
Dever 09 - Algoritmo de Prim

Objetivo:
Encontrar a menor rota de cabos de fibra óptica para conectar
todos os polos tecnológicos, utilizando o menor custo possível.
"""

import heapq


class Grafo:
    """Representa um grafo não direcionado e ponderado."""

    def __init__(self):
        self.adjacencias = {}

    def adicionar_aresta(self, origem, destino, peso):
        """Adiciona uma aresta entre dois vértices."""
        self.adjacencias.setdefault(origem, []).append((peso, origem, destino))
        self.adjacencias.setdefault(destino, []).append((peso, destino, origem))

    def prim(self, inicio):
        """Executa o Algoritmo de Prim."""
        visitados = set()
        fila_prioridade = []
        arvore_minima = []
        custo_total = 0

        visitados.add(inicio)

        for aresta in self.adjacencias[inicio]:
            heapq.heappush(fila_prioridade, aresta)

        while fila_prioridade and len(visitados) < len(self.adjacencias):
            peso, origem, destino = heapq.heappop(fila_prioridade)

            if destino not in visitados:
                visitados.add(destino)
                arvore_minima.append((origem, destino, peso))
                custo_total += peso

                for proxima_aresta in self.adjacencias[destino]:
                    if proxima_aresta[2] not in visitados:
                        heapq.heappush(fila_prioridade, proxima_aresta)

        return arvore_minima, custo_total


def main():
    """Função principal do programa."""
    grafo = Grafo()

    grafo.adicionar_aresta("A", "B", 4)
    grafo.adicionar_aresta("A", "C", 4)
    grafo.adicionar_aresta("B", "C", 2)
    grafo.adicionar_aresta("B", "D", 5)
    grafo.adicionar_aresta("C", "D", 5)
    grafo.adicionar_aresta("C", "E", 6)
    grafo.adicionar_aresta("D", "E", 3)
    grafo.adicionar_aresta("D", "F", 4)
    grafo.adicionar_aresta("E", "F", 2)

    rota, custo_total = grafo.prim("A")

    print("Rota dos cabos a serem instalados:")
    for origem, destino, peso in rota:
        print(f"{origem} - {destino}: {peso} km")

    print(f"\nQuantidade mínima de cabo utilizada: {custo_total} km")


if __name__ == "__main__":
    main()