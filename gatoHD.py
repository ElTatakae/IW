import random

# Función para imprimir el tablero
def print_board(board):
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("-----------")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("-----------")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])

# Función para obtener el puntaje de una posición del tablero
def get_score(position):
    if position in [0, 2, 6, 8]:
        return 3
    elif position == 4:
        return 4
    else:
        return 2

# Función para evaluar si hay un ganador
def get_winner(board):
    for i in range(0, 3):
        # Revisar filas
        if board[i*3] == board[i*3+1] == board[i*3+2] != " ":
            return board[i*3]
        # Revisar columnas
        if board[i] == board[i+3] == board[i+6] != " ":
            return board[i]
    # Revisar diagonales
    if board[0] == board[4] == board[8] != " ":
        return board[0]
    if board[2] == board[4] == board[6] != " ":
        return board[2]
    # No hay ganador
    return None

# Función para obtener la mejor jugada para la CPU
def get_best_move(board):
    # Buscar jugadas ganadoras
    for i in range(0, 9):
        if board[i] == " ":
            board[i] = "O"
            if get_winner(board) == "O":
                board[i] = " "
                return i
            board[i] = " "
    # Bloquear jugadas ganadoras del jugador
    for i in range(0, 9):
        if board[i] == " ":
            board[i] = "X"
            if get_winner(board) == "X":
                board[i] = " "
                return i
            board[i] = " "
    # Priorizar centro o esquinas según sea el caso
    if board[4] == " ":
        return 4
    if board[0] == "X" and board[8] == "X" or board[2] == "X" and board[6] == "X":
        for i in [1, 3, 5, 7]:
            if board[i] == " ":
                return i
    # Priorizar esquinas
    for i in [0, 2, 6, 8]:
        if board[i] == " ":
            return i
    # Tomar cualquier posición disponible
    for i in range(0, 9):
        if board[i] == " ":
            return i

# Función para jugar una partida
def play_game():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    turn = random.choice(["player", "cpu"])
    player_score = 0
    cpu_score = 0
    while True:
        print_board(board)
        winner = get_winner(board)
        if winner is not None:
            print_board(board)
            if winner == "X":
                player_score += 1
                print("¡Ganaste! Puntos del jugador:", player_score, " Puntos de la CPU:", cpu_score)
            else:
                cpu_score += 1
                print("¡Perdiste! Puntos del jugador:", player_score, " Puntos de la CPU:", cpu_score)
            play_again = input("¿Quieres jugar de nuevo? (s/n): ")
            if play_again.lower() == "s":
                play_game()
            else:
                break
        if turn == "player":
            # Turno del jugador
            print("Es tu turno (X)")
            while True:
                try:
                    position = int(input("Elige una posición (1-9): ")) - 1
                    if position < 0 or position > 8 or board[position] != " ":
                        print("Posición inválida. Por favor elige otra.")
                    else:
                        break
                except ValueError:
                    print("Entrada inválida. Por favor ingresa un número del 1 al 9.")
            board[position] = "X"
            turn = "cpu"
        else:
            # Turno de la CPU
            print("Turno de la CPU (O)")
            position = get_best_move(board)
            board[position] = "O"
            turn = "player"
