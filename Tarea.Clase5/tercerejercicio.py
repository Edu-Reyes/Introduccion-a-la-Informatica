"Bienvenido al programa de analisis de patente par o impar"

contador_par = 0
contador_impar = 0

while True:

    patente = input("Ingrese terminación de patente (0-9) o -1 para finalizar: ")

    if patente == "-1":
        break

    if not patente.isdigit():
        print("Ingrese un número válido.")
        continue

    patente = int(patente)

    if patente < 0 or patente > 9:
        print("La terminación debe estar entre 0 y 9.")
        continue

    if patente % 2 == 0:
        contador_par += 1
    else:
        contador_impar += 1

print("Patentes pares:", contador_par)
print("Patentes impares:", contador_impar)
