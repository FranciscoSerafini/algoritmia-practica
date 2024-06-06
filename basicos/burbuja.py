
def burbuja(lista):
    i = 0
    control = True
    while i <= len(lista)-2 and control:
        control = False
        for j in range(len(lista)-1-i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                control = True
        i = i + 1
    return lista

print(burbuja([1, 9, 5, 7, 2, 4, 8]))
#lista = []
