print("Bienvenido al sistema de un menú de pagos")

while True:
    precio = float(input("Ingrese el precio ($0 para salir): "))

    if precio == 0:
        print("Gracias por usar el programa")
        break

    print("1 - Efectivo")
    print("2 - Tarjeta 1 pago")
    print("3 - Tarjeta 3 pagos")
    print("4 - Tarjeta 6 pagos")

    opcion = int(input("Por favor seleccione una opción: "))

    if opcion == 1:
        total = precio * 0.9
        print(f"El total con descuento es de ${total} pesos")

    elif opcion == 2:
        print(f"El total es de ${precio} pesos")

    elif opcion == 3:
        total = precio * 1.15
        cuota = total / 3
        print(f"Serán 3 cuotas de ${round(cuota, 2)} pesos")

    elif opcion == 4:
        total = precio * 1.30
        cuota = total / 6
        print(f"Serán 6 cuotas de ${round(cuota, 2)} pesos")

    else:
        print("Opción inválida")