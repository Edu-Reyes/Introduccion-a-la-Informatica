print("BIenvendo al sistema de promedio de edades")

menores = 0
adultos = 0

suma_menores = 0
suma_adultos = 0

while True:
    edad = int(input("Ingrese la edad (-1 para salir): "))

    if edad == -1:
        break

    if edad < 0:
        print("Edad inválida")
    else:
        if edad < 18:
            menores += 1
            suma_menores += edad
        else:
            adultos += 1
            suma_adultos += edad

if menores > 0:
    promedio_menores = suma_menores / menores
else:
    promedio_menores = 0

if adultos > 0:
    promedio_adultos = suma_adultos / adultos
else:
    promedio_adultos = 0

print(f"Menores: {menores}")
print(f"Adultos: {adultos}")
print(f"Promedio de los menores: {promedio_menores}")
print(f"Promedio de los adultos: {promedio_adultos}")