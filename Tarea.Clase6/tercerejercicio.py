"Bienvenido al programa de separación de miles"

while True:
    numero = input("Ingrese un número grande: ")

    if numero.isdigit():
        break

    print("Error. Ingrese solo números.")

resultado = ""
contador = 0

for i in range(len(numero) - 1, -1, -1):

    resultado = numero[i] + resultado
    contador += 1

    if contador == 3 and i != 0:
        resultado = "." + resultado
        contador = 0

print(f"El resultado es {resultado}")