def pares_impares(numero):
    cont_impares = 0
    for i in range(1, numero + 1):
        if i % 2 == 0:
            print("Este numero es par:", i)
        else:
            print("Este numero es impar:", i)
            cont_impares += 1
    print("Cantidad de numero impares:", cont_impares)

pares_impares(10)