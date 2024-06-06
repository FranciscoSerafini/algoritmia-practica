
###recursividad###

def fibonacci(numero):
    if numero == 0 or numero == 1:
        return numero
    else:
        return fibonacci(numero-1) + fibonacci(numero - 2)

solucion = int(input("ingrese un numero:"))
print(fibonacci(solucion))