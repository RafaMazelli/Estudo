
def bubble_sort(lista):
    tamanho_lista = len(lista)
    for i in range(tamanho_lista):
        for j in range(tamanho_lista - 1):
            if lista[j + 1] < lista[j]:
                lista[j + 1], lista[j] = lista[j], lista[j + 1]


def insertion_sort(lista):
    tamanho_lista = len(lista)

    for i in range(tamanho_lista):
        item_analisado = lista[i]
        ind_ordenados = i - 1
        while ind_ordenados >= 0 and lista[ind_ordenados] > item_analisado:
            lista[ind_ordenados + 1] = lista[ind_ordenados]
            ind_ordenados -= 1
        lista[ind_ordenados + 1] = item_analisado


def selection_sort(lista):
    tamanho_lista = len(lista)

    for i in range(tamanho_lista):
        ind_menor_numero = i
        for j in range(i, tamanho_lista):
            if lista[j] < lista[ind_menor_numero]:
                ind_menor_numero = j
        if lista[i] > lista[ind_menor_numero]:
            aux = lista[i]
            lista[i] = lista[ind_menor_numero]
            lista[ind_menor_numero] = aux


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
    topo_esq, topo_dir = 0, 0
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
