print("Bienvenido al sistema de patentes")

pares = 0
impares = 0

while True:
    patente = int(input("Ingrese la terminación de la patente (-1 para salir): "))

    if patente == -1:
        break

    if patente < 0 or patente > 9:
        print("Error. Debe ingresar un número entre 0 y 9.")
    else:
        if patente % 2 == 0:
            pares += 1
        else:
            impares += 1

print(f"Patentes pares {pares}")
print(f"Patentes impares {impares}")