"""
Programa que nos permite generar contraseñas aleatorias.

Solo debes pasar como entrada la longitud maxima que quieres que tenga la contraseña.

Tambien puedes elegir si quieres guardar la contraseña en un archivo de texto.
"""

from random import choice

#funcion para guardar contraseña
def guardar_archivo(contenido):
    guardar = input("Desea guardar la contraseña en un archivo de texto, (SI,NO):")
    if guardar == "SI":
        with open("Contraseña.txt", "w") as archivo:
            archivo.write(contenido)
            archivo.close()
            print("Archivo creado correctamente")
    elif guardar == "NO":
        print("Programa Finalizado")
    else:
        print("Solo puedes contestar SI o NO")

longitud_contraseña = int(input("Especifique la longitud de la contraseña:"))
valores = "0123456789ABCDEFGHIJKLMNOPQRSTUWXYZabcdefghijklmnpqrstuvwxyz"

contraseña = ""
contraseña = contraseña.join([choice(valores) for i in range(longitud_contraseña)])
print("Su contraseña generada:", contraseña)
guardar_archivo(contraseña)

#JOIN: toma un iterable
#CHOICE: selecciona elementos al azar
#se crea una lista de valores con la contraseña


