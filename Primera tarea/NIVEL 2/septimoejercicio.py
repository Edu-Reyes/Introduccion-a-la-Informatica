print("Binevenido al programa que calcula el precio al cargar combustible")

while True:
    litros = float(input("Ingrese los litros cargados: "))

    print("1. Super")
    print("2. Premium")
    print("3. Diesel")
    print("4. Diesel Premium")

    opcion = int(input("Seleccione el combustible que quiere cargar: "))

    if litros <= 0:
        print("Cantidad inválida")
    else:
        if opcion == 1:
            precio = 120.3
        elif opcion == 2:
            precio = 147.3
        elif opcion == 3:
            precio = 113.4
        elif opcion == 4:
            precio = 145.9
        else:
            print("Opción inválida")
            continue

        total = litros * precio

        print(f"Importe total ${total} pesos")
        break