"""
Dever 07 - Heap Máxima.

Este programa demonstra passo a passo:
- inserção de elementos em uma Heap Máxima;
- comparações realizadas entre pais e filhos;
- trocas realizadas durante a organização;
- remoção do elemento de maior prioridade;
- reorganização da heap após cada remoção.
"""


class MaxHeap:
    """Representa uma estrutura de dados Heap Máxima."""

    def __init__(self):
        """Inicializa a Heap Máxima vazia."""
        self.heap = []

    def inserir(self, valor):
        """Insere um valor na heap e reorganiza a estrutura."""
        print(f"\nInserindo o elemento {valor} na heap.")

        self.heap.append(valor)

        print(f"Heap após inserir no final: {self.heap}")

        self._subir(len(self.heap) - 1)

        print(f"Heap organizada após inserção: {self.heap}")

    def remover_maximo(self):
        """Remove o maior elemento da heap e reorganiza a estrutura."""
        if not self.heap:
            print("A heap está vazia.")
            return None

        maior_elemento = self.heap[0]

        print(f"\nRemovendo o maior elemento: {maior_elemento}")

        if len(self.heap) == 1:
            self.heap.pop()
            print("Heap após remoção: []")
            return maior_elemento

        ultimo_elemento = self.heap.pop()
        self.heap[0] = ultimo_elemento

        print(f"Último elemento colocado na raiz: {ultimo_elemento}")
        print(f"Heap antes de reorganizar: {self.heap}")

        self._descer(0)

        print(f"Heap reorganizada após remoção: {self.heap}")

        return maior_elemento

    def _subir(self, indice):
        """Move o elemento inserido para cima enquanto necessário."""
        while indice > 0:
            indice_pai = (indice - 1) // 2

            print(
                f"Comparando filho {self.heap[indice]} "
                f"com pai {self.heap[indice_pai]}."
            )

            if self.heap[indice] > self.heap[indice_pai]:
                print(
                    f"Troca realizada: {self.heap[indice]} "
                    f"<-> {self.heap[indice_pai]}"
                )

                self.heap[indice], self.heap[indice_pai] = (
                    self.heap[indice_pai],
                    self.heap[indice],
                )

                indice = indice_pai
            else:
                print("Nenhuma troca necessária.")
                break

    def _descer(self, indice):
        """Move o elemento da raiz para baixo enquanto necessário."""
        tamanho = len(self.heap)

        while True:
            maior = indice
            esquerda = 2 * indice + 1
            direita = 2 * indice + 2

            if esquerda < tamanho:
                print(
                    f"Comparando pai {self.heap[maior]} "
                    f"com filho esquerdo {self.heap[esquerda]}."
                )

                if self.heap[esquerda] > self.heap[maior]:
                    maior = esquerda

            if direita < tamanho:
                print(
                    f"Comparando maior atual {self.heap[maior]} "
                    f"com filho direito {self.heap[direita]}."
                )

                if self.heap[direita] > self.heap[maior]:
                    maior = direita

            if maior != indice:
                print(
                    f"Troca realizada: {self.heap[indice]} "
                    f"<-> {self.heap[maior]}"
                )

                self.heap[indice], self.heap[maior] = (
                    self.heap[maior],
                    self.heap[indice],
                )

                indice = maior
            else:
                print("Nenhuma troca necessária.")
                break

    def mostrar_heap(self):
        """Exibe a heap atual."""
        print(f"Heap atual: {self.heap}")


def executar_heap():
    """Executa o exemplo solicitado no dever de casa."""
    elementos = [13, 2, 6, 25, 8, 40, 1]

    heap = MaxHeap()

    print("=== INSERÇÃO DOS ELEMENTOS ===")

    for elemento in elementos:
        heap.inserir(elemento)
        heap.mostrar_heap()

    print("\n=== REMOÇÃO DOS ELEMENTOS ===")

    while heap.heap:
        heap.remover_maximo()
        heap.mostrar_heap()


if __name__ == "__main__":
    executar_heap()