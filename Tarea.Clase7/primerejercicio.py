"Bienvenido al programa sobre el clima"

import random

def temperatura_minima(datos):
    return min(datos)

def temperatura_maxima(datos):
    return max(datos)

def temperatura_promedio(datos):
    return sum(datos) / len(datos)

def bajo_cero(datos):

    contador = 0

    for temperatura in datos:

        if temperatura < 0:
            contador += 1

    return contador

temperaturas = []

for i in range(30):

    temperatura = random.randint(-10, 40)
    temperaturas.append(temperatura)

print("Las temperaturas del mes:")
print(temperaturas)


print(f"La temperatura mínima: {temperatura_minima(temperaturas)}")
print(f"La temperatura máxima: {temperatura_maxima(temperaturas)}")
print(f"La temperatura promedio: {(temperatura_promedio(temperaturas))}")
print(f"La cantidad de temperaturas bajo cero: {bajo_cero(temperaturas)}")