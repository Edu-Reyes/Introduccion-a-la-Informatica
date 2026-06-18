"Bienvenido al programa de siempre distintos"

num1= input("Ingrese el primer número: ")

while not num1.isdigit():
    print("Por favor, ingrese solo números positivos.")
    num1= input("Ingrese el primer número: ")
num1 = int(num1)


num2= input("Ingrese el primer número: ")

while not num2.isdigit():
    print("Por favor, ingrese solo números positivos.")
    num2 = input("Ingrese el primer número: ")
num2 = int(num2)


num3= input("Ingrese el primer número: ")

while not num3.isdigit():
    print("Por favor, ingrese solo números positivos.")
    num3= input("Ingrese el primer número: ")
num3 = int(num3)

num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if num1 > num2 and num1 > num3:
    print("El mayor es:", num1)

elif num2 > num1 and num2 > num3:
    print("El mayor es:", num2)

else:
    print("El mayor es:", num3)