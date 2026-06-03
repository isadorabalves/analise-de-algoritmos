"""
Dever 13 - Redução de Ciclo Hamiltoniano para Caixeiro Viajante.

Objetivo:
    Demonstrar que um software capaz de resolver o Problema do Caixeiro
    Viajante também pode ser usado para resolver o problema do Ciclo
    Hamiltoniano.

Ideia da redução:
    Dado um grafo não direcionado G, construímos uma instância completa
    do TSP com os mesmos vértices.

    - Se existe aresta no grafo original, o custo é 1.
    - Se não existe aresta no grafo original, o custo é 2.

    Assim, G possui ciclo hamiltoniano se, e somente se, o menor ciclo do
    TSP tiver custo menor ou igual ao número de vértices.
"""

from dataclasses import dataclass
from itertools import permutations


EDGE_WEIGHT = 1
NON_EDGE_WEIGHT = 2


@dataclass(frozen=True)
class TspResult:
    """
    Representa o resultado retornado pelo resolvedor de TSP.

    Attributes:
        minimum_cost: Menor custo encontrado para o ciclo.
        path: Caminho correspondente ao ciclo encontrado.
    """

    minimum_cost: int
    path: tuple[int, ...]


class Graph:
    """
    Representa um grafo ponderado não direcionado sem pesos nas arestas.

    O grafo é usado como entrada do problema do Ciclo Hamiltoniano.
    """

    def __init__(self, vertices_count: int) -> None:
        """
        Inicializa o grafo com a quantidade informada de vértices.

        Args:
            vertices_count: Quantidade de vértices do grafo.
        """

        if vertices_count < 3:
            raise ValueError("O grafo precisa ter pelo menos 3 vértices.")

        self.vertices_count = vertices_count
        self._adjacency_list = [set() for _ in range(vertices_count)]

    def add_edge(self, first_vertex: int, second_vertex: int) -> None:
        """
        Adiciona uma aresta não direcionada entre dois vértices.

        Args:
            first_vertex: Primeiro vértice.
            second_vertex: Segundo vértice.
        """

        self._validate_vertex(first_vertex)
        self._validate_vertex(second_vertex)

        if first_vertex == second_vertex:
            raise ValueError("Não são permitidos laços no grafo.")

        self._adjacency_list[first_vertex].add(second_vertex)
        self._adjacency_list[second_vertex].add(first_vertex)

    def has_edge(self, first_vertex: int, second_vertex: int) -> bool:
        """
        Verifica se existe uma aresta entre dois vértices.

        Args:
            first_vertex: Primeiro vértice.
            second_vertex: Segundo vértice.

        Returns:
            True se a aresta existir; False caso contrário.
        """

        self._validate_vertex(first_vertex)
        self._validate_vertex(second_vertex)

        return second_vertex in self._adjacency_list[first_vertex]

    def _validate_vertex(self, vertex: int) -> None:
        """
        Valida se o vértice informado existe no grafo.

        Args:
            vertex: Vértice que será validado.
        """

        if vertex < 0 or vertex >= self.vertices_count:
            raise ValueError(f"Vértice inválido: {vertex}")


class BruteForceTspSolver:
    """
    Simula o software existente que resolve o problema do Caixeiro Viajante.

    A implementação usa força bruta apenas para fins didáticos.
    Em um cenário real, esta classe representaria o software já existente.
    """

    def solve(self, cost_matrix: list[list[int]]) -> TspResult:
        """
        Resolve uma instância do TSP buscando o ciclo de menor custo.

        Args:
            cost_matrix: Matriz de custos entre os vértices.

        Returns:
            Resultado contendo o menor custo e o caminho encontrado.
        """

        self._validate_cost_matrix(cost_matrix)

        vertices_count = len(cost_matrix)
        start_vertex = 0
        best_cost = float("inf")
        best_path = ()

        for permutation in permutations(range(1, vertices_count)):
            path = (start_vertex,) + permutation + (start_vertex,)
            cost = self._calculate_path_cost(path, cost_matrix)

            if cost < best_cost:
                best_cost = cost
                best_path = path

        return TspResult(minimum_cost=int(best_cost), path=best_path)

    def _calculate_path_cost(
        self,
        path: tuple[int, ...],
        cost_matrix: list[list[int]],
    ) -> int:
        """
        Calcula o custo total de um caminho no TSP.

        Args:
            path: Caminho percorrido.
            cost_matrix: Matriz de custos entre os vértices.

        Returns:
            Custo total do caminho.
        """

        total_cost = 0

        for index in range(len(path) - 1):
            origin = path[index]
            destination = path[index + 1]
            total_cost += cost_matrix[origin][destination]

        return total_cost

    def _validate_cost_matrix(self, cost_matrix: list[list[int]]) -> None:
        """
        Valida se a matriz de custos é quadrada.

        Args:
            cost_matrix: Matriz de custos que será validada.
        """

        if not cost_matrix:
            raise ValueError("A matriz de custos não pode estar vazia.")

        matrix_size = len(cost_matrix)

        for row in cost_matrix:
            if len(row) != matrix_size:
                raise ValueError("A matriz de custos precisa ser quadrada.")


class HamiltonianCycleToTspReduction:
    """
    Realiza a redução do Ciclo Hamiltoniano para o Caixeiro Viajante.
    """

    def build_cost_matrix(self, graph: Graph) -> list[list[int]]:
        """
        Constrói a matriz de custos do TSP a partir do grafo original.

        Args:
            graph: Grafo do problema do Ciclo Hamiltoniano.

        Returns:
            Matriz de custos equivalente para o TSP.
        """

        cost_matrix = []

        for origin in range(graph.vertices_count):
            row = []

            for destination in range(graph.vertices_count):
                if origin == destination:
                    row.append(0)
                elif graph.has_edge(origin, destination):
                    row.append(EDGE_WEIGHT)
                else:
                    row.append(NON_EDGE_WEIGHT)

            cost_matrix.append(row)

        return cost_matrix

    def has_hamiltonian_cycle(
        self,
        graph: Graph,
        tsp_solver: BruteForceTspSolver,
    ) -> tuple[bool, TspResult]:
        """
        Decide se o grafo possui Ciclo Hamiltoniano usando um resolvedor TSP.

        Args:
            graph: Grafo original.
            tsp_solver: Software capaz de resolver o TSP.

        Returns:
            Uma tupla contendo:
                - True ou False para existência de Ciclo Hamiltoniano;
                - o resultado retornado pelo resolvedor de TSP.
        """

        cost_matrix = self.build_cost_matrix(graph)
        tsp_result = tsp_solver.solve(cost_matrix)
        cost_limit = graph.vertices_count
        has_cycle = tsp_result.minimum_cost <= cost_limit

        return has_cycle, tsp_result


def create_graph_with_hamiltonian_cycle() -> Graph:
    """
    Cria um grafo que possui Ciclo Hamiltoniano.

    Returns:
        Grafo com ciclo hamiltoniano.
    """

    graph = Graph(vertices_count=4)

    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 0)

    return graph


def create_graph_without_hamiltonian_cycle() -> Graph:
    """
    Cria um grafo que não possui Ciclo Hamiltoniano.

    Returns:
        Grafo sem ciclo hamiltoniano.
    """

    graph = Graph(vertices_count=4)

    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)

    return graph


def format_path(path: tuple[int, ...]) -> str:
    """
    Formata o caminho para exibição no terminal.

    Args:
        path: Caminho retornado pelo resolvedor de TSP.

    Returns:
        Texto formatado com os vértices do caminho.
    """

    return " -> ".join(str(vertex) for vertex in path)


def show_result(title: str, graph: Graph) -> None:
    """
    Executa a redução e exibe o resultado no terminal.

    Args:
        title: Título do exemplo.
        graph: Grafo que será analisado.
    """

    tsp_solver = BruteForceTspSolver()
    reduction = HamiltonianCycleToTspReduction()

    has_cycle, tsp_result = reduction.has_hamiltonian_cycle(
        graph,
        tsp_solver,
    )

    answer = "Sim" if has_cycle else "Não"

    print("-" * 60)
    print(title)
    print(f"Existe ciclo hamiltoniano? {answer}")
    print(f"Menor custo encontrado no TSP: {tsp_result.minimum_cost}")
    print(f"Caminho retornado pelo TSP: {format_path(tsp_result.path)}")


def main() -> None:
    """
    Executa os exemplos da redução.
    """

    graph_with_cycle = create_graph_with_hamiltonian_cycle()
    graph_without_cycle = create_graph_without_hamiltonian_cycle()

    show_result("Exemplo 1: grafo com Ciclo Hamiltoniano", graph_with_cycle)
    show_result("Exemplo 2: grafo sem Ciclo Hamiltoniano", graph_without_cycle)


if __name__ == "__main__":
    main()