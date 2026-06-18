"Bienvenido al programa de inversión de un nombre"

nombre = input("Ingrese un nombre: ")

nombre_invertido = ""

for i in range(len(nombre) - 1, -1, -1):
    nombre_invertido += nombre[i]

print("El nombre invertido queda:", nombre_invertido)