print("Bienvenido al sistema que es un simmulador de caja")

total = 0
cantidad = 0

while True:
    precio = float(input("Ingrese el precio del producto (0 para terminar): "))

    if precio == 0:
        break

    if precio < 0:
        print("Precio inválido")
    else:
        total += precio
        cantidad += 1

print(f"La cantidad de productos es de: {cantidad}")
print(f"El total a pagar es de ${total} pesos")