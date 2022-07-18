# vou utilizar aqui para fazer rascunhos como ja spoilei pelo nome do arquivo né hehehe
# im gonna use this file just as sketch (dont know a better word than sketch. thx google translate:) )

teste = [43,2,5,44,333,6,55,44,343,23]

def bubble_sort(lista):
    tamanho_lista = len(lista)
    for i in range(tamanho_lista - 1):
        for j in range(tamanho_lista-1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]


print(teste)
print('-' * 50)
bubble_sort(teste)
print(teste)


