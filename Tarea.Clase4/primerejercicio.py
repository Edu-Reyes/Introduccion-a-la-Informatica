"Bienvenido al programa de ingreso=0"

while True:
    precio = input("Ingrese el precio del producto (0 para salir): ")

    if precio.isdigit():
        precio = float(precio)

        if precio == 0:
            print("Gracias por usar el programa.")
            break

        if precio < 0:
            print("El precio no puede ser negativo.")
            continue
    else:
        print("Ingrese un número válido.")
        continue

    while True:
        importe = input("Ingrese el importe pagado: ")

        if importe.isdigit():
            importe = float(importe)

            if importe < 0:
                print("El importe no puede ser negativo.")
                continue
            break
        else:
            print("Ingrese un número válido.")

    if importe < precio:
        print("Dinero insuficiente.")
    elif importe == precio:
        print("Pago justo.")
    else:
        vuelto = importe - precio
        print("Vuelto: $", vuelto, "pesos")
