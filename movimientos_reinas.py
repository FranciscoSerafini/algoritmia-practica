def es_valido(tablero, fila, columna):
    # Verifica si es seguro colocar una reina en el tablero en la posición (fila, columna)
    
    # Verificación de la columna
    for i in range(fila):
        if tablero[i] == columna:
            return False
    
    # Verificación de la diagonal izquierda
    for i, j in zip(range(fila - 1, -1, -1), range(columna - 1, -1, -1)):
        if tablero[i] == j:
            return False
    
    # Verificación de la diagonal derecha
    for i, j in zip(range(fila - 1, -1, -1), range(columna + 1, len(tablero))):
        if tablero[i] == j:
            return False

    return True

def resolver_n_reinas(tablero, fila):
    # Función recursiva para resolver el problema de las N reinas
    
    # Si todas las reinas han sido colocadas, retorna True
    if fila >= len(tablero):
        return True
    
    # Itera sobre todas las columnas en la fila actual
    for columna in range(len(tablero)):
        # Verifica si es seguro colocar una reina en esta posición
        if es_valido(tablero, fila, columna):
            # Coloca una reina en la posición (fila, columna)
            tablero[fila] = columna
            # Intenta colocar las reinas restantes
            if resolver_n_reinas(tablero, fila + 1):
                return True
            # Si no es posible colocar una reina en esta posición, retrocede
            tablero[fila] = -1
    
    # Si no se puede colocar ninguna reina en esta fila, retorna False
    return False

def n_reinas(n):
    # Función principal para encontrar la solución del problema de las N reinas
    
    # Crea un tablero vacío con valores -1
    tablero = [-1] * n
    # Llama a la función recursiva para resolver el problema
    if resolver_n_reinas(tablero, 0):
        return tablero
    else:
        return None
    
# Solicita al usuario que ingrese el número de reinas
n = int(input("Ingrese un número de reinas: "))
# Encuentra una solución para el problema de las N reinas
solucion = n_reinas(n)

# Muestra la solución encontrada o un mensaje si no hay solución
if solucion:
    print(f'Solución para {n} reinas: {solucion}')
else:
    print(f'No hay solución para {n} reinas')

