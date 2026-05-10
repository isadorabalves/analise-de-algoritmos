# Dever 07 — Heap Máxima (Max Heap)

## Objetivo

Demonstrar passo a passo a inserção e remoção de elementos em uma estrutura Heap Máxima (Max Heap), utilizando a lista:

```python
[13, 2, 6, 25, 8, 40, 1]
```

O exercício apresenta:

- Comparações realizadas;
- Trocas (swap);
- Organização da árvore após cada inserção;
- Processo de remoção do maior elemento;
- Reorganização da heap após cada remoção.

---

# Conceito de Heap Máxima

Uma Heap Máxima é uma árvore binária completa onde:

- O pai sempre possui valor maior que os filhos;
- O maior elemento sempre fica na raiz.

Exemplo:

```text
        40
      /    \
    13      25
   /  \    /  \
  2    8  6    1
```

---

# Inserções Passo a Passo

## Inserção do 13

Heap:

```python
[13]
```

Árvore:

```text
13
```

---

## Inserção do 2

2 é inserido como filho de 13.

Comparação:

```text
2 < 13
```

Nenhuma troca necessária.

Heap:

```python
[13, 2]
```

Árvore:

```text
   13
  /
 2
```

---

## Inserção do 6

6 é inserido como filho de 13.

Comparação:

```text
6 < 13
```

Nenhuma troca necessária.

Heap:

```python
[13, 2, 6]
```

Árvore:

```text
    13
   /  \
  2    6
```

---

## Inserção do 25

25 entra na próxima posição disponível.

Estado inicial:

```python
[13, 2, 6, 25]
```

Comparações:

```text
25 > 2
```

Troca realizada:

```python
[13, 25, 6, 2]
```

Nova comparação:

```text
25 > 13
```

Nova troca realizada:

```python
[25, 13, 6, 2]
```

Árvore:

```text
       25
      /  \
    13    6
   /
  2
```

---

## Inserção do 8

Estado inicial:

```python
[25, 13, 6, 2, 8]
```

Comparação:

```text
8 < 13
```

Nenhuma troca necessária.

Árvore:

```text
       25
      /  \
    13    6
   / \
  2   8
```

---

## Inserção do 40

Estado inicial:

```python
[25, 13, 6, 2, 8, 40]
```

Comparações:

```text
40 > 6
```

Troca realizada:

```python
[25, 13, 40, 2, 8, 6]
```

Nova comparação:

```text
40 > 25
```

Nova troca realizada:

```python
[40, 13, 25, 2, 8, 6]
```

Árvore:

```text
        40
      /    \
    13      25
   /  \    /
  2    8  6
```

---

## Inserção do 1

Estado inicial:

```python
[40, 13, 25, 2, 8, 6, 1]
```

Comparação:

```text
1 < 25
```

Nenhuma troca necessária.

Heap final:

```python
[40, 13, 25, 2, 8, 6, 1]
```

Árvore:

```text
        40
      /    \
    13      25
   /  \    /  \
  2    8  6    1
```

---

# Remoções Passo a Passo

## Remoção do 40

O maior elemento sempre é removido da raiz.

Último elemento substitui a raiz:

```python
[1, 13, 25, 2, 8, 6]
```

Comparações:

```text
25 > 13
25 > 1
```

Troca realizada:

```python
[25, 13, 1, 2, 8, 6]
```

Nova comparação:

```text
6 > 1
```

Nova troca realizada:

```python
[25, 13, 6, 2, 8, 1]
```

Árvore:

```text
        25
      /    \
    13      6
   /  \    /
  2    8  1
```

---

## Remoção do 25

Substituindo a raiz pelo último elemento:

```python
[1, 13, 6, 2, 8]
```

Comparações:

```text
13 > 6
13 > 1
```

Troca realizada:

```python
[13, 1, 6, 2, 8]
```

Nova comparação:

```text
8 > 2
8 > 1
```

Nova troca realizada:

```python
[13, 8, 6, 2, 1]
```

Árvore:

```text
       13
      /  \
     8    6
    / \
   2   1
```

---

## Remoção do 13

Substituindo a raiz pelo último elemento:

```python
[1, 8, 6, 2]
```

Comparações:

```text
8 > 6
8 > 1
```

Troca realizada:

```python
[8, 1, 6, 2]
```

Nova comparação:

```text
2 > 1
```

Nova troca realizada:

```python
[8, 2, 6, 1]
```

Árvore:

```text
      8
     / \
    2   6
   /
  1
```

---

# Complexidade

## Inserção

A inserção em uma Heap Máxima possui complexidade:

```text
O(log n)
```

Isso acontece porque o elemento inserido pode precisar subir até a raiz da árvore.

---

## Remoção

A remoção do maior elemento também possui complexidade:

```text
O(log n)
```

Isso acontece porque, após remover a raiz, o novo elemento colocado no topo pode precisar descer pela árvore.

---

# Conclusão

A Heap Máxima é uma estrutura eficiente para trabalhar com prioridades, pois mantém sempre o maior elemento na raiz.

Neste exercício, foram demonstrados:

- Inserção dos elementos;
- Comparações entre pais e filhos;
- Trocas realizadas durante a organização;
- Remoção do maior elemento;
- Reorganização da heap após cada remoção.