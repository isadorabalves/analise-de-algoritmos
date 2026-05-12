"""
Módulo contendo a implementação do algoritmo de Floyd-Warshall.
Este algoritmo encontra os caminhos mais curtos entre todos os pares
de vértices em um grafo ponderado.
"""

# Constante para representar a ausência de conexão (infinito)
INF = float('inf')

class GraphShortestPath:
    """
    Classe para calcular e gerenciar os caminhos mais curtos em um grafo.

    Utiliza o algoritmo de Floyd-Warshall para processar a matriz de
    adjacência e encontrar as menores distâncias possíveis.
    """

    def __init__(self, vertices_count):
        """
        Inicializa o grafo determinando seu tamanho.

        Args:
            vertices_count (int): O número total de vértices presentes no grafo.
        """
        self.vertices_count = vertices_count

    def floyd_warshall(self, graph_matrix):
        """
        Aplica o algoritmo de Floyd-Warshall na matriz fornecida.

        Args:
            graph_matrix (list of list of float): Matriz de adjacência
                que representa os pesos das arestas do grafo.

        Returns:
            list of list of float: Matriz resultante contendo as menores
                distâncias entre cada par de vértices.
        """
        # Inicializa a matriz de distâncias fazendo uma cópia da matriz original
        distance_matrix = [list(row) for row in graph_matrix]

        # Algoritmo principal (3 loops aninhados)
        # k = vértice intermediário, i = vértice de origem, j = vértice de destino
        for k in range(self.vertices_count):
            for i in range(self.vertices_count):
                for j in range(self.vertices_count):
                    # Se o caminho passando por 'k' for menor, atualiza a distância
                    if distance_matrix[i][k] + distance_matrix[k][j] < distance_matrix[i][j]:
                        distance_matrix[i][j] = distance_matrix[i][k] + distance_matrix[k][j]

        return distance_matrix

    def print_solution(self, distance_matrix):
        """
        Imprime a matriz de distâncias de forma formatada e legível no terminal.

        Args:
            distance_matrix (list of list of float): A matriz resolvida a ser impressa.
        """
        print("Matriz das menores distâncias entre cada par de vértices:")
        for i in range(self.vertices_count):
            row_output = []
            for j in range(self.vertices_count):
                if distance_matrix[i][j] == INF:
                    row_output.append(f"{'INF':>5}")
                else:
                    row_output.append(f"{distance_matrix[i][j]:>5}")
            print(" ".join(row_output))


# Execução prática para testar a implementação
if __name__ == "__main__":
    # Matriz de adjacência de exemplo baseada em um grafo direcionado
    # 0 indica distância para si mesmo, INF indica que não há aresta direta
    GRAPH_EXAMPLE = [
        [0,   5,  INF, 10],
        [INF, 0,   3,  INF],
        [INF, INF, 0,   1],
        [INF, INF, INF, 0]
    ]

    total_vertices = 4
    
    # Instanciando a classe
    shortest_path_solver = GraphShortestPath(total_vertices)
    
    # Executando o algoritmo
    result_matrix = shortest_path_solver.floyd_warshall(GRAPH_EXAMPLE)
    
    # Imprimindo o resultado
    shortest_path_solver.print_solution(result_matrix)