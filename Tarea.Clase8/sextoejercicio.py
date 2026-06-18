"Bienvenido al programa sobre un temporizador"

import time


def pedir_valor(mensaje, maximo):

    while True:

        try:
            valor = int(input(mensaje))

            if 0 <= valor <= maximo:
                return valor

            print("Fuera del rango.")

        except:
            print("Ingrese un entero.")


hora = pedir_valor("Horas: ", 23)
minuto = pedir_valor("Minutos: ", 59)
segundo = pedir_valor("Segundos: ", 59)

while hora > 0 or minuto > 0 or segundo > 0:

    print(f"{hora:02}:{minuto:02}:{segundo:02}")

    time.sleep(1)

    segundo -= 1

    if segundo < 0:

        segundo = 59
        minuto -= 1

        if minuto < 0:

            minuto = 59
            hora -= 1

print("00:00:00")
print("<<<< TIEMPO >>>>")