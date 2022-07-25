
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




