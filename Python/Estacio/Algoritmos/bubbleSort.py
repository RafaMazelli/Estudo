#implementando o bubble sort em python
#implementing bubble sort with python

#well, i guess i dont have not much to say about this one. It just compares n-1  times the itens with his adjacent ones sorting in a crescent way
import random

def bubble_sort(lista):
    tamanho_lista = len(lista) 
    for i in range(tamanho_lista - 1): #o conjunto de ambos os comandos for faz com que todos os itens sejam verificados n-1 vezes, menos o ultimo elemento porque nao precisa
        for j in range(tamanho_lista - 1):
            if lista[j] > lista[j + 1]: # aqui é a condição que ira verificar se o item adjacente é maior
                lista[j], lista[j + 1] = lista[j + 1], lista[j] #aqui ocorre a troca de lugar entre o item analisado e seu adjacente caso seja maior


#-=-=-=-=-=-=-=TESTANDO O ALGORITMO=-=-=-=-=-=-=-
#-=-=-=-=-=-=-=TESTING THE ALGORITHM=-=-=-=-=-=-=-
array_de_numeros_aleatorios = random.sample(range(1,2000), 15)

ordenados = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

invertidos = [15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]

repetidos = [3,2,1,1,5,4,6,2,3,8,6,5,8,6,8]

lista = array_de_numeros_aleatorios
print('=-' * 25)
print(f'\33[1;31mLista >> {lista}\33[m')
print('v-' * 25)
bubble_sort(lista)
print(f'\33[1;32mLista Ordenada >> {lista}\33[m')
print('=-' * 25)
