"Bienvenido al programa que analiza números"

import random


def analizar(secreto, intento):

    correctos = 0
    aproximados = 0

    for i in range(4):

        if intento[i] == secreto[i]:
            correctos += 1

        elif intento[i] in secreto:
            aproximados += 1

    return correctos, aproximados


secreto = str(random.randint(1000, 9999))

while True:

    intento = input("Ingrese un número de 4 cifras (-1 salir): ")

    if intento == "-1":
        print("Juego terminado.")
        break

    if not intento.isdigit():
        print("Ingrese solo números.")
        continue

    if len(intento) != 4:
        print("Debe tener 4 cifras.")
        continue

    correctos, aproximados = analizar(secreto, intento)

    print(correctos, "correctos y", aproximados, "aproximados")

    if correctos == 4:
        print("¡Ganaste!")
        break