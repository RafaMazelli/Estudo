#implementando insertion sort em python
#implementing insertion sort with python
#O selection sort elege o elemento de menor valor e o coloca na sua devida posição

import random

def selection_sort(lista):
    tamanho_lista = len(lista)

    for j in range(tamanho_lista - 1):
        indice_menor_numero = j
        for i in range(j, tamanho_lista):
            if lista[i] < lista[indice_menor_numero]:
                indice_menor_numero = i
        if lista[j] > lista[indice_menor_numero]:
            aux = lista[j]
            lista[j] = lista[indice_menor_numero]
            lista[indice_menor_numero] = aux


#-=-=-=-=-=-=-=TESTANDO O ALGORITMO=-=-=-=-=-=-=-
#-=-=-=-=-=-=-=TESTING THE ALGORITHM=-=-=-=-=-=-=-
array_de_numeros_aleatorios = random.sample(range(1,2000), 15)

ordenados = [1,2,3,4,5,6,7,8,9]

invertidos = [15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]

repetidos = [3,2,1,1,5,4,6,2,3,8,6,5,8,6,8]

lista = array_de_numeros_aleatorios
print('=-' * 25)
print(f'\33[1;31mLista >> {lista}\33[m')
print('v-' * 25)
selection_sort(lista)
print(f'\33[1;32mLista Ordenada >> {lista}\33[m')
print('=-' * 25)
