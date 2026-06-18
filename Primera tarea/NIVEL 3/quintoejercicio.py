print("BIevenido al sistema para ver el nombre invertido")

nombre = input("Ingrese un nombre: ")

invertido = ""

for i in range(len(nombre) - 1, -1, -1):
    invertido += nombre[i]

print(f"El nombre invertido queda: {invertido}")