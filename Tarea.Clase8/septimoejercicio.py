"Bienvenido al programa sobre repetición de números"

#Primer manera
import random


while True:

    try:
        num = int(input("Cantidad de números (1-101): "))

        if 1 <= num <= 101:
            break

        print("Fuera de rango.")

    except:
        print("Ingrese un entero.")


lista = []

while len(lista) < num:

    numero = random.randint(0, 100)

    if numero not in lista:
        lista.append(numero)

print(lista)

#Segunda manera

import random


while True:

    try:
        num = int(input("Cantidad de números (1-101): "))

        if 1 <= num <= 101:
            break

        print("Fuera de rango.")

    except:
        print("Ingrese un entero.")


lista = []

while len(lista) < num:

    lista.append(random.randint(0, 100))

    lista = list(set(lista))

print(lista)