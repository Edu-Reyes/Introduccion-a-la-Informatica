"Bienvenido al programa de calculo factorial"

numero = input("Ingrese un número entero mayor o igual a 0: ")

while not numero.isdigit():
    print("Ingrese un número válido.")
    numero = input("Ingrese un número entero mayor o igual a 0: ")

numero = int(numero)

factorial = 1

for i in range(1, numero + 1):
    factorial *= i

print("El factorial de", numero, "es", factorial)
