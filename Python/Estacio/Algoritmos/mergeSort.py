import random



def merge_sort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)
    
    if (fim - inicio > 1):
        meio = (inicio + fim) // 2
        merge_sort(lista, inicio, meio)
        merge_sort(lista, meio, fim)
        merge(lista, inicio, meio, fim)


def merge(lista, inicio, meio, fim):
    esquerda = lista[inicio:meio]
    direita = lista[meio:fim]
    index_top_esquerda, index_top_direita = 0, 0
    for i in range(inicio, fim):
        if index_top_esquerda >= len(esquerda):
            lista[i] = direita[index_top_direita]
            index_top_direita += 1
        elif index_top_direita >= len(direita):
            lista[i] = esquerda[index_top_esquerda]
            index_top_esquerda += 1
        elif esquerda[index_top_esquerda] < direita[index_top_direita]:
            lista[i] = esquerda[index_top_esquerda]
            index_top_esquerda += 1
        else:
            lista[i] = direita[index_top_direita]
            index_top_direita += 1




#-=-=-=-=-=-=-=TESTANDO O ALGORITMO=-=-=-=-=-=-=-
#-=-=-=-=-=-=-=TESTING THE ALGORITHM=-=-=-=-=-=-=-
array_de_numeros_aleatorios = random.sample(range(1,2000), 15)

ordenados = [1,2,3,4,5,6,7,8,9]

invertidos = [15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]

repetidos = [3,2,1,1,5,4,6,2,3,8,6,5,8,6,8]

lista = repetidos
print('=-' * 25)
print(f'\33[1;31mLista >> {lista}\33[m')
print('v-' * 25)
merge_sort(lista)
print(f'\33[1;32mLista Ordenada >> {lista}\33[m')
print('=-' * 25)