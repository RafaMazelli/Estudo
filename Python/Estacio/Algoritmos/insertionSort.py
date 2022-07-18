#implementando insertion sort em python
import random

def insertionSort(lista):
    tamanhoLista = len(lista)
    for i in range(1,tamanhoLista):
        chave = lista[i]
        indice_elemento_ordenado = i - 1
        while indice_elemento_ordenado >= 0 and lista[indice_elemento_ordenado] > chave:
            lista[indice_elemento_ordenado + 1] = lista[indice_elemento_ordenado]
            indice_elemento_ordenado = indice_elemento_ordenado - 1
        lista[indice_elemento_ordenado + 1] = chave



array_de_numeros_aleatorios = random.sample(range(1,2000), 180)

print(array_de_numeros_aleatorios)
print('=-' * 15)
insertionSort(array_de_numeros_aleatorios)
print('=-' * 15)
print(array_de_numeros_aleatorios)