# Dever 13 - Redução de Ciclo Hamiltoniano para Caixeiro Viajante

## Problema A

Ciclo Hamiltoniano.

O objetivo é descobrir se um grafo possui um ciclo que passa por todos os
vértices exatamente uma vez e retorna ao vértice inicial.

## Problema B

Caixeiro Viajante.

O objetivo é encontrar o ciclo de menor custo que passa por todos os vértices
exatamente uma vez e retorna ao ponto inicial.

## Redução

Para resolver o problema A usando um software que resolve o problema B, fazemos
a seguinte transformação:

1. Recebemos um grafo não direcionado `G`.
2. Criamos uma instância completa do TSP com os mesmos vértices de `G`.
3. Para cada par de vértices:
   - se a aresta existe em `G`, atribuímos custo `1`;
   - se a aresta não existe em `G`, atribuímos custo `2`.
4. Executamos o resolvedor de TSP.
5. Se o menor custo encontrado for menor ou igual ao número de vértices, então
   existe Ciclo Hamiltoniano no grafo original.
6. Caso contrário, não existe Ciclo Hamiltoniano.

## Justificativa

Se o grafo original possui Ciclo Hamiltoniano, então existe um ciclo que usa
apenas arestas reais do grafo. Como cada aresta real recebe custo `1`, o custo
total desse ciclo será igual ao número de vértices.

Por outro lado, se o TSP retorna um ciclo com custo menor ou igual ao número de
vértices, então todas as arestas usadas no ciclo possuem custo `1`. Isso significa
que todas elas existem no grafo original. Portanto, esse ciclo também é um Ciclo
Hamiltoniano no grafo original.

Assim:

```text
G possui Ciclo Hamiltoniano se, e somente se, a instância do TSP possui ciclo
com custo menor ou igual a |V|.