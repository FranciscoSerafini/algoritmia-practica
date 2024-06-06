###CRIPTOGRAFIA###

abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

cadena_cifra = str(input("Escribe la cadena que quieras cifrar:")).upper()
clave_cifra = int(input("Escribe la clave que quieres cifrar:"))

texto_cifrado = " "

for letras in cadena_cifra:
    if letras == "":
        texto_cifrado += " "
    else:
        x = abc.find(letras) + clave_cifra
        mod = int(x)%26 #por si sobre pasa el rango
        texto_cifrado = texto_cifrado + str(abc[mod])

print(texto_cifrado)

