"""
Dever 14 - Implementação do Algoritmo de Bellman-Ford.

Objetivos:
    - Calcular menores caminhos a partir do vértice A.
    - Realizar o relaxamento das arestas.
    - Exibir a tabela de atualização das distâncias.
    - Detectar ciclo negativo.
"""


INF = float("inf")


class Graph:
    """
    Representa um grafo direcionado e ponderado.
    """

    def __init__(self) -> None:
        """
        Inicializa o grafo com uma lista vazia de arestas.
        """

        self.edges = []
        self.vertices = set()

    def add_edge(self, origin: str, destination: str, weight: int) -> None:
        """
        Adiciona uma aresta ao grafo.

        Args:
            origin: Vértice de origem.
            destination: Vértice de destino.
            weight: Peso da aresta.
        """

        self.edges.append((origin, destination, weight))
        self.vertices.add(origin)
        self.vertices.add(destination)


class BellmanFord:
    """
    Executa o algoritmo de Bellman-Ford em um grafo.
    """

    def __init__(self, graph: Graph, source: str) -> None:
        """
        Inicializa as distâncias e predecessores.

        Args:
            graph: Grafo utilizado no algoritmo.
            source: Vértice de origem.
        """

        self.graph = graph
        self.source = source
        self.distances = {}
        self.predecessors = {}

        for vertex in graph.vertices:
            self.distances[vertex] = INF
            self.predecessors[vertex] = None

        self.distances[source] = 0

    def run(self) -> None:
        """
        Executa o Bellman-Ford e exibe as tabelas de relaxamento.
        """

        vertices_count = len(self.graph.vertices)

        self.show_initial_state()

        for iteration in range(1, vertices_count):
            print(f"\nIteração {iteration}")

            for origin, destination, weight in self.graph.edges:
                self.relax(origin, destination, weight)

            self.show_table()

        print("\nVerificando ciclo negativo...")

        if self.has_negative_cycle():
            print("Ciclo negativo detectado!")
        else:
            print("Não há ciclo negativo.")

    def relax(self, origin: str, destination: str, weight: int) -> None:
        """
        Realiza o relaxamento de uma aresta.

        Args:
            origin: Vértice de origem.
            destination: Vértice de destino.
            weight: Peso da aresta.
        """

        origin_distance = self.distances[origin]
        destination_distance = self.distances[destination]

        if origin_distance != INF and origin_distance + weight < destination_distance:
            new_distance = origin_distance + weight
            self.distances[destination] = new_distance
            self.predecessors[destination] = origin

            print(
                f"Relaxando {origin}->{destination}: "
                f"{origin_distance} + {weight} < {destination_distance} "
                f"-> Atualizar {destination} = {new_distance}"
            )

    def has_negative_cycle(self) -> bool:
        """
        Verifica se existe ciclo negativo no grafo.

        Returns:
            True se existir ciclo negativo; False caso contrário.
        """

        for origin, destination, weight in self.graph.edges:
            origin_distance = self.distances[origin]
            destination_distance = self.distances[destination]

            if origin_distance != INF and origin_distance + weight < destination_distance:
                return True

        return False

    def show_initial_state(self) -> None:
        """
        Exibe o estado inicial das distâncias.
        """

        print("Estado inicial:")
        self.show_table()

    def show_table(self) -> None:
        """
        Exibe a tabela atual de distâncias e predecessores.
        """

        ordered_vertices = sorted(self.graph.vertices)

        print("\nTabela de distâncias:")
        print("Vértice | Distância | Predecessor")
        print("-" * 33)

        for vertex in ordered_vertices:
            distance = self.distances[vertex]
            predecessor = self.predecessors[vertex]

            distance_text = "∞" if distance == INF else str(distance)
            predecessor_text = "-" if predecessor is None else predecessor

            print(f"{vertex:^7} | {distance_text:^9} | {predecessor_text:^10}")


def create_graph() -> Graph:
    """
    Cria o grafo solicitado no dever.

    Returns:
        Grafo com as arestas informadas na atividade.
    """

    graph = Graph()

    graph.add_edge("A", "B", 1)
    graph.add_edge("A", "C", 4)
    graph.add_edge("B", "C", 2)
    graph.add_edge("B", "D", 5)
    graph.add_edge("C", "D", 1)
    graph.add_edge("C", "E", 3)
    graph.add_edge("D", "C", -3)
    graph.add_edge("D", "E", 2)
    graph.add_edge("E", "D", 1)

    return graph


def main() -> None:
    """
    Função principal do programa.
    """

    graph = create_graph()
    bellman_ford = BellmanFord(graph, source="A")
    bellman_ford.run()


if __name__ == "__main__":
    main()