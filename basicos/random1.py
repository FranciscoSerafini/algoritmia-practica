import random

def obtener_respuestas(numero):
    if numero == 1:
        print('Es seguro')
    elif numero == 2:
        print('Decididamente es asi')
    elif numero == 3:
        print('Francisco es asi')
    elif numero == 4:
        print('El perro es asi')
    elif numero == 5:
        print('Francisco serafini es asi')

respuesta = random.randint(1,5)
print(obtener_respuestas(respuesta))

print('Hola', end=" ")
print('Mundo')
print('peros','gatos','francisco', sep=',')
