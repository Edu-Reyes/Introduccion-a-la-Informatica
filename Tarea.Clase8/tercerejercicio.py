"Bienvenido al programa que calcula raíces cuadráticas"

import math

print("Cálculo de raíces cuadráticas. Por favor, siga los siguientes pasos")

def ingreso_numero(datos):

    while True:

        try:
            return float(input(datos))

        except ValueError:
            print("Ingrese un número válido.")


def calcular_raices(a, b, c):

    discriminante = b ** 2 - 4 * a * c

    if discriminante < 0:
        return None

    x1 = (-b + math.sqrt(discriminante)) / (2 * a)
    x2 = (-b - math.sqrt(discriminante)) / (2 * a)

    return x1, x2


while True:

    a = ingreso_numero("Ingrese A: ")

    if a != 0:
        break

    print("a no puede ser cero.")

b = ingreso_numero("Ingrese B: ")
c = ingreso_numero("Ingrese C: ")

resultado = calcular_raices(a, b, c)

if resultado == None:
    print("Las raíces son imaginarias.")
else:
    print("Raíz 1:", resultado[0])
    print("Raíz 2:", resultado[1])