import random
import time

def insertion_sort(lista):
    
    for i in range(1, len(lista)):

        atual = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > atual:
            lista[j + 1] = lista[j]
            j = j - 1
       
        lista[j + 1] =  atual
tamanhos = [1000, 5000, 10000, 20000, 50000]

for n in tamanhos:

    lista = [random.randint(0, 100000) for _ in range(n)]

    lista_insertion = lista.copy()
    inicio = time.time()
    insertion_sort(lista_insertion)
    fim = time.time()
    tempo_insertion = fim - inicio

    lista_sorted = lista.copy()
    inicio = time.time()
    sorted(lista_sorted)
    fim = time.time()
    tempo_sorted = fim - inicio

    print("n =", n,
          "| insertion =", tempo_insertion, "segundos",
          "| sorted =", tempo_sorted, "segundos")