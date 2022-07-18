#implementando insertion sort em python
#implementing insertion sort with python

import random

def insertion_sort(lista):
    tamanho_lista = len(lista) #pegando o tamanho da lista 
    for i in range(1,tamanho_lista):
        item_analisado = lista[i] # variavel utilizada para armazenar o valor do numero analisado 
        indice_ordenados = i - 1 #indice que irá representar a porção ordenada a esquerda do numero analisado
        while indice_ordenados >= 0 and lista[indice_ordenados] > item_analisado: #Este while irá verificar onde o numero analisado irá se encaixar na porção ordenada que está a esquerda dele
            lista[indice_ordenados + 1] = lista[indice_ordenados] # Este comando chega o valor uma posição a direita dentro do vetor
            indice_ordenados -= 1 #decrementando o valor do indice para a esquerda em direção ao proximo item da porção ordenada
        lista[indice_ordenados + 1] = item_analisado #Aqui é onde o item analisado é inserido no seu devido lugar com o detalhe de que colocamos ele um indice a frente do ultimo numero analisado na porção dos já ordenados. 
       

#-=-=-=-=-=-=-=TESTANDO O ALGORITMO=-=-=-=-=-=-=-
#-=-=-=-=-=-=-=TESTING THE ALGORITHM=-=-=-=-=-=-=-
array_de_numeros_aleatorios = random.sample(range(1,2000), 15)

ordenados = [1,2,3,4,5,6,7,8,9]

invertidos = [15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]

repetidos = [3,2,1,1,5,4,6,2,3,8,6,5,8,6,8]

lista = invertidos
print('=-' * 25)
print(f'\33[1;31mLista >> {lista}\33[m')
print('v-' * 25)
insertion_sort(lista)
print(f'\33[1;32mLista Ordenada >> {lista}\33[m')
print('=-' * 25)