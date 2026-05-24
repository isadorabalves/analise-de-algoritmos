"""
Dever 11 — Grafo e Dijkstra

Objetivo:
1. Gerar automaticamente um grafo com:
   - 50 nós
   - 150 arestas

2. Implementar o algoritmo de Dijkstra.

3. Encontrar o menor caminho entre
   o Nó 1 e o Nó 50.

4. Exibir no terminal:
   - Grafo gerado
   - Menor caminho
   - Custo total

"""

import heapq
import random


# ==========================
# Configurações do grafo
# ==========================

TOTAL_NOS = 50
TOTAL_ARESTAS = 150

PESO_MINIMO = 1
PESO_MAXIMO = 20


class Grafo:
    """
    Representa um grafo ponderado
    não direcionado utilizando
    lista de adjacências.
    """

    def __init__(self):
        """
        Inicializa o grafo vazio.
        """
        self.adjacencias = {
            no: []
            for no in range(
                1,
                TOTAL_NOS + 1
            )
        }

        self.arestas = set()

    def adicionar_aresta(
        self,
        origem,
        destino,
        peso
    ):
        """
        Adiciona uma aresta entre
        dois nós do grafo.

        Args:
            origem (int):
                Nó de origem

            destino (int):
                Nó destino

            peso (int):
                Peso da aresta

        Returns:
            bool:
                True caso adicione
                False caso exista
        """

        aresta = tuple(
            sorted(
                (origem, destino)
            )
        )

        if origem == destino:
            return False

        if aresta in self.arestas:
            return False

        self.arestas.add(aresta)

        self.adjacencias[
            origem
        ].append(
            (destino, peso)
        )

        self.adjacencias[
            destino
        ].append(
            (origem, peso)
        )

        return True

    def gerar_grafo(self):
        """
        Gera automaticamente
        um grafo conectado
        contendo:

        - 50 nós
        - 150 arestas
        """

        # Garante conectividade
        for no in range(
            1,
            TOTAL_NOS
        ):

            peso = random.randint(
                PESO_MINIMO,
                PESO_MAXIMO
            )

            self.adicionar_aresta(
                no,
                no + 1,
                peso
            )

        # Completa até 150 arestas
        while len(
            self.arestas
        ) < TOTAL_ARESTAS:

            origem = random.randint(
                1,
                TOTAL_NOS
            )

            destino = random.randint(
                1,
                TOTAL_NOS
            )

            peso = random.randint(
                PESO_MINIMO,
                PESO_MAXIMO
            )

            self.adicionar_aresta(
                origem,
                destino,
                peso
            )


def reconstruir_caminho(
    anteriores,
    inicio,
    fim
):
    """
    Reconstrói o caminho
    encontrado pelo algoritmo.

    Args:
        anteriores:
            Dicionário dos nós anteriores

        inicio:
            Nó inicial

        fim:
            Nó final

    Returns:
        list:
            Caminho encontrado
    """

    caminho = []

    no_atual = fim

    while no_atual is not None:

        caminho.append(
            no_atual
        )

        no_atual = anteriores[
            no_atual
        ]

    caminho.reverse()

    if caminho[0] != inicio:
        return []

    return caminho


def dijkstra(
    grafo,
    inicio,
    fim
):
    """
    Executa o algoritmo
    de Dijkstra.

    Args:
        grafo:
            Objeto Grafo

        inicio:
            Nó inicial

        fim:
            Nó destino

    Returns:
        tuple:
            Caminho e custo
    """

    distancias = {
        no: float("inf")
        for no in grafo.adjacencias
    }

    anteriores = {
        no: None
        for no in grafo.adjacencias
    }

    distancias[inicio] = 0

    fila = [
        (0, inicio)
    ]

    while fila:

        distancia_atual, no_atual = (
            heapq.heappop(
                fila
            )
        )

        if no_atual == fim:
            break

        if (
            distancia_atual >
            distancias[no_atual]
        ):
            continue

        for (
            vizinho,
            peso
        ) in grafo.adjacencias[
            no_atual
        ]:

            nova_distancia = (
                distancia_atual +
                peso
            )

            if (
                nova_distancia <
                distancias[vizinho]
            ):

                distancias[
                    vizinho
                ] = nova_distancia

                anteriores[
                    vizinho
                ] = no_atual

                heapq.heappush(
                    fila,
                    (
                        nova_distancia,
                        vizinho
                    )
                )

    caminho = reconstruir_caminho(
        anteriores,
        inicio,
        fim
    )

    custo = distancias[fim]

    return caminho, custo


def imprimir_grafo(
    grafo
):
    """
    Exibe o grafo
    no terminal.
    """

    print("\n")
    print("=" * 50)

    print("GRAFO GERADO")

    print(
        f"Nós: {TOTAL_NOS}"
    )

    print(
        f"Arestas: "
        f"{len(grafo.arestas)}"
    )

    print("=" * 50)

    for no in grafo.adjacencias:

        conexoes = []

        for (
            destino,
            peso
        ) in grafo.adjacencias[
            no
        ]:

            texto = (
                f"{destino}"
                f"(peso={peso})"
            )

            conexoes.append(
                texto
            )

        print(
            f"{no}: "
            f"{', '.join(conexoes)}"
        )


def imprimir_resultado(
    caminho,
    custo
):
    """
    Imprime o menor caminho
    encontrado.
    """

    print("\n")
    print("=" * 50)

    print(
        "MENOR CAMINHO "
        "(NÓ 1 → NÓ 50)"
    )

    print("=" * 50)

    rota = " -> ".join(
        map(
            str,
            caminho
        )
    )

    print(
        f"Caminho: {rota}"
    )

    print(
        f"Custo total: "
        f"{custo}"
    )


def main():
    """
    Função principal
    do programa.
    """

    grafo = Grafo()

    grafo.gerar_grafo()

    inicio = 1
    fim = 50

    caminho, custo = (
        dijkstra(
            grafo,
            inicio,
            fim
        )
    )

    imprimir_grafo(
        grafo
    )

    imprimir_resultado(
        caminho,
        custo
    )


if __name__ == "__main__":
    main()