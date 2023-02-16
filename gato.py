import random

# Función para dibujar el tablero
def dibujar_tablero(tablero):
    print(f"{tablero[0]} | {tablero[1]} | {tablero[2]}")
    print("--+---+--")
    print(f"{tablero[3]} | {tablero[4]} | {tablero[5]}")
    print("--+---+--")
    print(f"{tablero[6]} | {tablero[7]} | {tablero[8]}")

# Función para determinar si un jugador ha ganado
def hay_ganador(tablero):
    # Comprobar filas
    for i in range(0, 9, 3):
        if tablero[i] == tablero[i+1] == tablero[i+2] and tablero[i] != " ":
            return tablero[i]
    # Comprobar columnas
    for i in range(3):
        if tablero[i] == tablero[i+3] == tablero[i+6] and tablero[i] != " ":
            return tablero[i]
    # Comprobar diagonales
    if tablero[0] == tablero[4] == tablero[8] and tablero[0] != " ":
        return tablero[0]
    if tablero[2] == tablero[4] == tablero[6] and tablero[2] != " ":
        return tablero[2]
    # Si no hay ganador
    return None

# Función para obtener la lista de casillas disponibles
def obtener_casillas_disponibles(tablero):
    casillas_disponibles = []
    for i in range(9):
        if tablero[i] == " ":
            casillas_disponibles.append(i)
    return casillas_disponibles

# Función para que el CPU haga su movimiento
def movimiento_cpu(tablero):
    casillas_disponibles = obtener_casillas_disponibles(tablero)
    if 4 in casillas_disponibles: # Si el centro está disponible, jugar allí
        return 4
    # Si no, seleccionar aleatoriamente una casilla disponible
    return random.choice(casillas_disponibles)

# Función para obtener la puntuación de una casilla
def obtener_puntuacion_casilla(casilla):
    if casilla == 4: # El centro
        return 4
    elif casilla in [0, 2, 6, 8]: # Esquinas
        return 3
    else: # Lados restantes
        return 2

# Función principal del juego
def jugar_gato():
    # Inicializar el tablero y el turno
    tablero = [" "] * 9
    turno = random.choice(["Jugador", "CPU"])
    print(f"El {turno} inicia el juego.")
    dibujar_tablero(tablero)
    while True:
        if turno == "Jugador":
            # Turno del jugador
            casilla_jugador = int(input("Elige una casilla (0-8): "))
            while casilla_jugador not in obtener_casillas_disponibles(tablero):
                print("Casilla inválida.")
                casilla_jugador = int(input("Elige una casilla (0-8): "))
            tablero[casilla_jugador] = "X"
            dibujar_tablero(tablero)
            ganador = hay_ganador(tablero)
            if ganador:
                print(f"{ganador} ha ganado.")
                return
            if len(obtener_casillas_disponibles(tablero)) == 0:
                print("Empate.")
                return
            turno = "CPU"
        else:
            # Turno del CPU
            print("Turno del CPU.")
            casilla_cpu = movimiento_cpu(tablero)
            puntuacion_casilla_cpu = obtener_puntuacion_casilla(casilla_cpu)
            tablero[casilla_cpu] = "O"
            print(f"El CPU elige la casilla {casilla_cpu} (puntuación: {puntuacion_casilla_cpu}).")
            dibujar_tablero(tablero)
            ganador = hay_ganador(tablero)
            if ganador:
                print(f"{ganador} ha ganado.")
                return
            if len(obtener_casillas_disponibles(tablero)) == 0:
                print("Empate.")
                return
            turno = "Jugador"

# Ejecutar el juego
jugar_gato()
