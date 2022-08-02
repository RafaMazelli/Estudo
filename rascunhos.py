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
            indice_ordenados -= 1
        lista[indice_ordenados + 1] = item_analisado

def selection_sort(lista):
    tamanho_lista = len(lista)
    for i in range(tamanho_lista):
        menor_indice = i
        for j in range(i, tamanho_lista):
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
        merge_sort(lista, meio, fim)
        merge(lista, inicio, meio, fim)

def merge(lista, inicio, meio, fim):
    esquerda = lista[inicio:meio]
    direita = lista[meio:fim]
    top_dir, top_esq = 0, 0

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
    pass

print(teste)
print('-' * 50)
merge_sort(teste)
print(teste)
