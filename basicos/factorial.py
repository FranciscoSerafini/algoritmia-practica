###recursividad## 

def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)

solucion = int(input("Ingrese un numero para saber su factorial:"))
print(factorial(solucion))