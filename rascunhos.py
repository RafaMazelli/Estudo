# vou utilizar aqui para fazer rascunhos como ja spoilei pelo nome do arquivo né hehehe
# im gonna use this file just as sketch (dont know a better word than sketch. thx google translate:) )



teste = [43, 2, 5, 44, 333, 6, 55, 44, 343, 23]


def selection_sort(lista):
    tamanho = len(lista)
    for i in range(tamanho - 1):
        index_min = i
        for j in range(i, tamanho):
            if lista[j] < lista[index_min]:
                index_min = j
        if lista[i] > lista[index_min]:
            aux = lista[i]
            lista[i] = lista[index_min]
            lista[index_min] = aux

print(teste)
print('-' * 50)
selection_sort(teste)
print(teste)
