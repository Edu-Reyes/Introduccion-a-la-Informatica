"Bienvenido al programa de adivinar números"

import random

secreto = random.randint(1000, 9999)

while True:

    try:

        intento = int(input("Ingrese un número de 4 cifras (-1 salir): "))

        if intento == -1:
            print("Juego terminado.")
            break

        if intento < 1000 or intento > 9999:
            print("Debe tener 4 cifras.")
            continue

        if intento == secreto:
            print("¡Adivinaste!")
            break

        if intento > secreto:
            print("El número secreto es menor.")
        else:
            print("El número secreto es mayor.")

    except:
        print("Ingrese un número válido.")
