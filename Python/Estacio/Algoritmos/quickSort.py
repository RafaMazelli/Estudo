# using this file to save the right way of this algorithm

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
    return barra_menores


teste = [1,5,4,2,55,1,22,3232]
print(teste)
print('-=' * 20)
quick_sort(teste)
print(teste)