print ("Bienvenido al programa de límite de boleto")

precio = float(input("Ingrese el precio del boleto: "))

cantidad = int(input("Ingrese la cantidad de boletos: "))

while cantidad < 1:
    print("La cantidad debe ser mayor a 0")
    cantidad = int(input("Ingrese la cantidad de boletos: "))

if cantidad >= 5:
    print("Lo siento, ese es el limite del cupo")
else:
    total = precio * cantidad
    print(f"Total a pagar es ${total} pesos")