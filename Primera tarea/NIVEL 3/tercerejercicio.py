print("Bienveniod al programa que calcula el factorial")

while True:
    numero = int(input("Ingrese un número positivo: "))

    if numero >= 0:
        break
    else:
        print("Error. Debe ser positivo.")

factorial = 1

for i in range(1, numero + 1):
    factorial *= i

print(f"El factorial es {factorial}")