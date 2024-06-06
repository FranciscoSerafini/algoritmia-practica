def seleccion(lista):
    for i in range(len(lista)-1):
        min = i
        for j in range(i+ 1, len(lista)):
            if lista[j] < lista[min]:
                min = j
        lista[i], lista[min] = lista[min], lista[i]
    return lista

print(seleccion([1, 9, 5, 7, 2, 4, 8]))
            