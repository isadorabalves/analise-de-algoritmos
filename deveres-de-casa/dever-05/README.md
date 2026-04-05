# Dever 05 - Análise de Algoritmos

## Objetivo
Apresentar o cálculo de complexidade para:

1. Merge Sort
2. Multiplicação de matrizes
3. Recorrências

---

## 1. Merge Sort

O algoritmo Merge Sort utiliza a estratégia de divisão e conquista.

### Funcionamento
- Divide a lista em partes menores;
- Ordena cada parte recursivamente;
- Junta (merge) as partes ordenadas.

### Complexidade
- Tempo: O(n log n)
- Espaço: O(n)

---

## 2. Multiplicação de Matrizes

A multiplicação de matrizes combina linhas da matriz A com colunas da matriz B.

### Funcionamento
- Cada elemento da matriz resultado é calculado pela soma dos produtos.

### Complexidade
- Tempo: O(n³)
- Espaço: O(n²)

---

## 3. Recorrências

As recorrências foram resolvidas utilizando o Teorema Mestre.

### Resultados
- T(n) = 2T(n/4) + √n → Θ(√n log n)
- T(n) = 2T(n/4) + n → Θ(n)
- T(n) = 16T(n/4) + n² → Θ(n² log n)

---

## Como executar

No terminal, dentro da pasta dever-05:

```bash
python merge_sort.py
python matrizes.py
python recorrencias.py