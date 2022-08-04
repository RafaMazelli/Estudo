# Sorting Algorithms

def bubble_sort(lista):
    # the bubble sort algorithm compares the next element of the array with the current, switching their positions if crescent or decrescent
    tamanho_lista = len(lista)
    # o conjunto de ambos os comandos for faz com que todos os itens sejam verificados n-1 vezes, menos o ultimo elemento porque nao precisa
    for i in range(tamanho_lista - 1):
        for j in range(tamanho_lista - 1):
            # aqui é a condição que ira verificar se o item adjacente é maior
            if lista[j] > lista[j + 1]:
                # aqui ocorre a troca de lugar entre o item analisado e seu adjacente caso seja maior
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


def insertion_sort(lista):
    # the insertion sort algorithm grabs the next element of the array and compares with the previous ones to put it in the right spot (crescent or decrescent ways)
    tamanho_lista = len(lista)  # pegando o tamanho da lista
    for i in range(1, tamanho_lista):
        # variavel utilizada para armazenar o valor do numero analisado
        item_analisado = lista[i]
        # indice que irá representar a porção ordenada a esquerda do numero analisado
        indice_ordenados = i - 1
        # Este while irá verificar onde o numero analisado irá se encaixar na porção ordenada que está a esquerda dele
        while indice_ordenados >= 0 and lista[indice_ordenados] > item_analisado:
            # Este comando chega o valor uma posição a direita dentro do vetor
            lista[indice_ordenados + 1] = lista[indice_ordenados]
            # decrementando o valor do indice para a esquerda em direção ao proximo item da porção ordenada
            indice_ordenados -= 1
        # Aqui é onde o item analisado é inserido no seu devido lugar com o detalhe de que colocamos ele um indice a frente do ultimo numero analisado na porção dos já ordenados.
        lista[indice_ordenados + 1] = item_analisado


def selection_sort(lista):
    # The selection sort searchs for the element with less(or higher.. it depends) value and switching position with the current one
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
    # This merge sort algorithm works spliting the array recursively until it is just one item, then it merges all back together sorting them in a crescent or decrescent way

    if fim is None:
        fim = len(lista)

    if (fim - inicio > 1):
        meio = (inicio + fim) // 2
        merge_sort(lista, inicio, meio)
        merge_sort(lista, meio, fim)
        merge(lista, inicio, meio, fim)


def merge(lista, inicio, meio, fim):
    # Here is the step of merging from the merge sort algorithm
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


def quick_sort(lista, inicio=0, fim=None):
    """
    The quick sort algorithm works selecting a random item from the array, the pivot, and we will put all the itens that has less values behind it and consequently the itens who has higher value automatically will be after the pivot. The thing is to decide the best way to select the pivot to optimize the sorting. Here i coded to select always the last element of the array.
    """

    if fim is None:
        fim = len(lista) - 1 #just used this condition because in python we cannot use functions as parameters and the minus 1 is because we will use the "fim" variable as parameter in range function, otherwise it would catch the out of range index 

    if inicio < fim:
        p = partition(lista, inicio, fim)
        quick_sort(lista, inicio, p - 1)
        quick_sort(lista, p + 1, fim)


def partition(lista, inicio, fim):
    """
    The step of the quick sort algorithm that selects the pivot and switches the position of the itens.

    """
    pivot = lista[fim] 
    barra_menores = inicio 
    for barra_maiores in range(inicio, fim):
        if lista[barra_maiores] <= pivot:
            lista[barra_maiores], lista[barra_menores] = lista[barra_menores], lista[barra_maiores]
            barra_menores += 1
    lista[barra_menores], lista[fim] = lista[fim], lista[barra_menores]
    return barra_menores
