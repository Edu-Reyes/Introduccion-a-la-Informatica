"Bienvenido al programa de tabla de multiplicar"

numero = input("Ingrese un número entero: ")

while not numero.isdigit():
    print("Ingrese un número válido.")
    numero = input("Ingrese un número entero: ")

numero = int(numero)

suma = 0

for i in range(1, 13):

    resultado = numero * i

    print(numero, "x", i, "=", resultado)

    suma += resultado

print("Suma de los resultados:", suma)