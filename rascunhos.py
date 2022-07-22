# vou utilizar aqui para fazer rascunhos como ja spoilei pelo nome do arquivo né hehehe
# im gonna use this file just as sketch (dont know a better word than sketch. thx google translate:) )

teste = [43, 2, 5, 44, 333, 6, 55, 44, 343, 23]


def insertion_sort(lista):
    t = len(lista)
    for i in range(t):
        item_analisado = lista[i]
        indice_ordenados = i - 1
        while indice_ordenados >= 0 and lista[indice_ordenados] > item_analisado:
            lista[indice_ordenados + 1] = lista[indice_ordenados]
            indice_ordenados -= 1
        lista[indice_ordenados + 1] = item_analisado


print(teste)
print('-' * 50)
insertion_sort(teste)
print(teste)
