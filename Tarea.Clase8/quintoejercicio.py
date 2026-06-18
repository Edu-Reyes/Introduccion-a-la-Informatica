"Bienvenido al programa sobre un reloj digital"

import time


def pedir_hora():

    while True:

        try:
            hora = int(input("Hora (0-23): "))

            if 0 <= hora <= 23:
                return hora

            print("Hora inválida.")

        except:
            print("Ingrese un entero.")


def pedir_min_seg(mensaje):

    while True:

        try:
            valor = int(input(mensaje))

            if 0 <= valor <= 59:
                return valor

            print("Valor inválido.")

        except:
            print("Ingrese un entero.")


hora = pedir_hora()
minuto = pedir_min_seg("Minuto: ")
segundo = pedir_min_seg("Segundo: ")

while True:

    print(f"{hora:02}:{minuto:02}:{segundo:02}")

    time.sleep(1)

    segundo += 1

    if segundo == 60:
        segundo = 0
        minuto += 1

    if minuto == 60:
        minuto = 0
        hora += 1

    if hora == 24:
        hora = 0