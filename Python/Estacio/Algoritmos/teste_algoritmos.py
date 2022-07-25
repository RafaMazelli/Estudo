import random
from algoritmos_de_ordenacao import bubble_sort, insertion_sort, selection_sort, merge_sort, merge

# -=-=-=-=-=-=-=TESTANDO O ALGORITMO=-=-=-=-=-=-=-
# -=-=-=-=-=-=-=TESTING THE ALGORITHM=-=-=-=-=-=-=-
array_de_numeros_aleatorios = random.sample(range(1, 2000), 15)

ordenados = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

invertidos = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

repetidos = [3, 2, 1, 1, 5, 4, 6, 2, 3, 8, 6, 5, 8, 6, 8]

lista = repetidos
print('=-' * 25)
print(f'\33[1;31mLista >> {lista}\33[m')
print('v-' * 25)
merge_sort(lista)
print(f'\33[1;32mLista Ordenada >> {lista}\33[m')
print('=-' * 25)
