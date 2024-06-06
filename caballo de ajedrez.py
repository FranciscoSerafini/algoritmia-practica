# Definimos los movimientos válidos para cada posición del teclado numérico
mapeo = {
    1: [6, 8],
    2: [7, 9],
    3: [4, 8],
    4: [3, 9, 0],
    5: [],
    6: [1, 7, 0],
    7: [2, 6],
    8: [1, 3],
    9: [2, 4],
    0: [4, 6]
}

def contar_movimientos(inicio, mov_izq, move_map, memo):
    # Si no quedan movimientos, es un camino válido
    if mov_izq == 0:
        return 1
    
    # Verificamos si el resultado ya está memorizado
    if (inicio, mov_izq) in memo:
        return memo[(inicio, mov_izq)]
    
    total_moves = 0
    
    # Recorrer todos los movimientos posibles desde la posición actual
    #implmenta la recursion de llamar a la funcion asi misma
    for mov_siguiente in move_map[inicio]:
        total_moves += contar_movimientos(mov_siguiente, mov_izq - 1, move_map, memo)
    
    # Memorizamos el resultado
    memo[(inicio, mov_izq)] = total_moves
    return total_moves

def mov_validos_totales(num_moves):
    move_map = {
        1: [6, 8],
        2: [7, 9],
        3: [4, 8],
        4: [3, 9, 0],
        5: [],
        6: [1, 7, 0],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4],
        0: [4, 6]
    }
    total_moves = 0
    memorizacion = {}
    
    # Calcular movimientos válidos comenzando desde cada posición
    for inicio in range(10):
        total_moves += contar_movimientos(inicio, num_moves, move_map, memorizacion)
    
    return total_moves

# Ejecución del algoritmo para diferentes valores de `k`
results = []
for i in range(1, 9):
    results.append((i, mov_validos_totales(i)))
    
# Imprimir los resultados
for result in results:
    print(f"Para {result[0]} movimientos, hay {result[1]} movimientos válidos.")
