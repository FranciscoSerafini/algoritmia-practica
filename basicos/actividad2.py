###Implementar una función que calcule la suma de todos los números enteros comprendidos entre cero y un número entero positivo dado.

def sumatoria(numero):
    suma = 0
    for i in range(numero + 1):
        suma += i
    return suma

solucion = int(input("Ingrese un numero entero:"))
print(sumatoria(solucion))

