"Bienvenido al programa sobre combinaciones de fichas"

import math

def calcular_combinaciones(fichas):
    return math.factorial(len(fichas))

lista = []

while True:

    ficha = input("Ingrese una ficha. Escriba FIN para terminar: ").upper()

    if ficha == "FIN":

        if len(lista) > 0:
            break

        print("Por favor, ingrese al menos una ficha.")

    else:
        lista.append(ficha)

print(f"Cantidad de combinaciones: {calcular_combinaciones(lista)}")