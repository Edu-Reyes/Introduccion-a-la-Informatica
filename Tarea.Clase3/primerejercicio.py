"Bienvenido al programa de venta de boletos"

precio = float(input("Ingrese el precio del boleto: "))

cantidad = input("Ingrese la cantidad de boletos: ")

while not cantidad.isdigit():
    cantidad = input("Error. Ingrese una cantidad válida: ")

cantidad = int(cantidad)

if cantidad >= 5:
    print("No se puede realizar la venta. Cupo limitado.")
else:
    total = precio * cantidad
    print("Total a pagar: $", total, "pesos")