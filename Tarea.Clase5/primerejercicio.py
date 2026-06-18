"Bienvenido al programa de mayor y menor número"

menor = None
mayor = None

while True:

    numero = input("Ingrese un número positivo (-1 para finalizar): ")

    if numero == "-1":
        break

    if not numero.isdigit():
        print("Ingrese un número válido.")
        continue

    numero = int(numero)

    if menor is None or numero < menor:
        menor = numero

    if mayor is None or numero > mayor:
        mayor = numero

if menor is None:
    print("No se ingresaron números.")
else:
    print("Menor número:", menor)
    print("Mayor número:", mayor)