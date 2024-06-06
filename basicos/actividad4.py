###Implementar una función para calcular la potencia dado dos números enteros, el primero representa
##la base y segundo el exponente

def potencia(base,exponente):
    return base**exponente

base = int(input("Ingrese la base:"))
exponente = int(input("Ingrese el exponente:"))

print(potencia(base,exponente))