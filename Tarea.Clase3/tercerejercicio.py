"Bienvenido al programa de limite de crédito"

limite= float(input("Ingrese el límite actual: "))

tipo = input("Ingrese el tipo de tarjeta (1, 2, 3 u otro): ")

while not tipo.isdigit():
    tipo = input("Error. Ingrese un número de tipo de tarjeta: ")

tipo = int(tipo)

if tipo == 1:
    nuevo_limite = limite * 1.25

elif tipo == 2:
    nuevo_limite = limite * 1.35

elif tipo == 3:
    nuevo_limite = limite * 1.40

else:
    nuevo_limite = limite * 1.50

print("Nuevo límite: $", nuevo_limite, "pesos")