# vou utilizar aqui para fazer rascunhos como ja spoilei pelo nome do arquivo né hehehe
# im gonna use this file just as sketch (dont know a better word than sketch. thx google translate:) )


<<<<<<< HEAD

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
=======
teste = [43, 2, 5, 44, 333, 6, 55, 44, 343, 23]


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
    topo_dir, topo_esq = 0, 0
    for i in range(inicio, fim):
        if topo_esq >= len(esquerda):
            lista[i] = direita[topo_dir]
            topo_dir += 1
        elif topo_dir >= len(direita):
            lista[i] = esquerda[topo_esq]
            topo_esq += 1
        elif esquerda[topo_esq] < direita[topo_dir]:
            lista[i] = esquerda[topo_esq]
            topo_esq += 1
        else:
            lista[i] = direita[topo_dir]
            topo_dir += 1


print(teste)
print('-' * 50)
merge_sort(teste)
>>>>>>> 2fafa89e2ac18d917dc691c64602b6024c27ae95
print(teste)
