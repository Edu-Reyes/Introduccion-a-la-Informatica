"Bienvenido al programa de cálculo de área de circulos"

import math

def ingreso_radio():

    while True:

        try:
            radio = float(input("Ingrese el radio: "))

            if radio > 0:
                return radio

            print("El radio debe ser mayor que cero.")

        except:
            print("Ingrese un número válido.")

def calcular_area(radio):
    return math.pi * radio ** 2

radio = ingreso_radio()

print(f"El área es: {calcular_area(radio)}")