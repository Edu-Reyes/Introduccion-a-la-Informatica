"Bienvenido al programa de estadistica de edades"

enores = 0
mayores = 0
suma_menores = 0
suma_mayores = 0

while True:

    edad = input("Ingrese una edad (-1 para finalizar): ")

    if edad == "-1":
        break

    if not edad.isdigit():
        print("Ingrese un número para la edad.")
        continue

    edad = int(edad)

    if edad < 0 or edad > 100:
        print("Ingrese un número para la edad.")
        continue

    if edad < 18:
        menores += 1
        suma_menores += edad
    else:
        mayores += 1
        suma_mayores += edad

print("Menores de 18:", menores)
print("Mayores o iguales a 18:", mayores)

if menores > 0:
    print("Promedio de menores:", suma_menores / menores)
else:
    print("No hubo menores.")

if mayores > 0:
    print("Promedio de mayores:", suma_mayores / mayores)
else:
    print("No hubo mayores.")