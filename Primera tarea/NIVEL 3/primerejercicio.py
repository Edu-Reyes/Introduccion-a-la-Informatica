print("Bienvenido al programa de tabla de multiplicar")

numero = int(input("Ingrese un número: "))

suma = 0

for i in range(1, 13):
    resultado = numero * i
    suma = suma + resultado
    print(f"{numero} x {i} = {resultado}")

print(f"La suma total es {suma}")