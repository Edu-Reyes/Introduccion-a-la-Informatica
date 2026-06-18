"Bienvenido al programa sobre el juego Ludo"

import random


def pedir_tablerito():

    while True:

        try:
            tamaño = int(input("Tamaño del tablero (5-25): "))

            if 5 <= tamaño <= 25:
                return tamaño

            print("Debe estar entre 5 y 25.")

        except:
            print("Ingrese un entero válido.")


def mover_jugador(tablero, posicion, nombre):

    dado = random.randint(1, 6)

    print(f"Dado N°: {dado}")

    tablero[posicion] = "_"

    posicion += dado

    if posicion >= len(tablero):
        posicion = len(tablero) - 1

    tablero[posicion] = nombre

    print(tablero)

    return posicion


tamaño = pedir_tablerito()

j1 = ["_"] * tamaño
j2 = ["_"] * tamaño

j1[0] = "J1"
j2[0] = "J2"

pos1 = 0
pos2 = 0

while True:

    input("Turno J1. Aprete Enter para tirar el dado")
    pos1 = mover_jugador(j1, pos1, "J1")

    if pos1 == tamaño - 1:
        print("Ganó J1")
        break

    input("Turno J2. Aprete Enter para tirar el dado")
    pos2 = mover_jugador(j2, pos2, "J2")

    if pos2 == tamaño - 1:
        print("Ganó J2")
        break