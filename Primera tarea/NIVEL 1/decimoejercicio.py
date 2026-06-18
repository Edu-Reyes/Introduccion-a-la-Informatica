print("Bienvendo al programa que calcula el área de un círculo")

radio = input("Ingrese el radio: ")

while not radio.isdigit():
    print("Error, ingrese solo números")
    radio = input("Ingrese el radio: ")

radio = int(radio)

pi = 3.14

area = pi * (radio * radio)

print(f"El área del círculo es {area}")