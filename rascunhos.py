# vou utilizar aqui para fazer rascunhos como ja spoilei pelo nome do arquivo né hehehe
# im gonna use this file just as sketch (dont know a better word than sketch. thx google translate:) )



teste = [43, 2, 5, 44, 333, 6, 55, 44, 343, 23]


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
        indice_ordenados = i - 1
        while indice_ordenados >= 0 and lista[indice_ordenados] > item_analisado:
            lista[indice_ordenados + 1] = lista[indice_ordenados]
            i -= 1
        lista[indice_ordenados + 1] = item_analisado


def selection_sort(lista):
    tamanho_lista = len(lista)
    for i in range(tamanho_lista - 1):
        menor_indice = 0
        for j in range(tamanho_lista):
            if lista[j] < lista[menor_indice]:
                menor_indice = j
        if lista[i] > lista[menor_indice]:
            aux = lista[i]
            lista[i] = lista[menor_indice]
            lista[menor_indice] = aux

def merge_sort(lista, inicio=0, fim=None):
    
    if fim is None:
        fim = len(lista)

    if (fim - inicio > 1):
        meio = (inicio + fim) // 2
        merge_sort(lista, inicio, meio)
        merge_sort(lista, meio, inicio)
        merge(lista, inicio, meio, fim)

def merge(lista, inicio, meio, fim):
    esquerda = lista[inicio:meio]
    direita = lista[meio:fim]
    top_esq, top_dir = 0, 0
    for i in range(inicio, fim):
        if top_esq >= len(esquerda):
            lista[i] = direita[top_dir]
            top_dir += 1
        
        elif top_dir >= len(direita):
            lista[i] = esquerda[top_esq]
            top_esq += 1

        elif esquerda[top_esq] < direita[top_dir]:
            lista[i] = esquerda[top_esq]
            top_esq += 1

        else:
            lista[i] = direita[top_dir]
            top_dir += 1

def quick_sort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1

    if inicio < fim:
        p = partition(lista, inicio, fim)
        quick_sort(lista, inicio, p - 1)
        quick_sort(lista, p + 1, fim)

def partition(lista, inicio, fim):
    pivot = lista[fim]
    barra_menores = inicio
    for barra_maiores in range(inicio, fim):
        if lista[barra_maiores] <= pivot:
            lista[barra_maiores], lista[barra_menores] = lista[barra_menores], lista[barra_maiores]
            barra_menores += 1
    lista[barra_menores], lista[fim] = lista[fim], lista[barra_menores]
    return lista[barra_menores]

print(teste)
print('-' * 50)
quick_sort(teste)
print(teste)
