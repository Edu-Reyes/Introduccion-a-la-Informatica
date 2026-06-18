print("Bienvenido al programa de límite de crédito")

while True:
    limite = float(input("Ingrese el límite actual: "))
    tipo = int(input("Ingrese el tipo de tarjeta: "))

    if limite <= 0:
        print("Por favor, ingrese un límite válido")
    else:
        if tipo == 1:
            aumento = limite * 0.25
        elif tipo == 2:
            aumento = limite * 0.35
        elif tipo == 3:
            aumento = limite * 0.40
        else:
            aumento = limite * 0.50

        nuevo_limite = limite + aumento

        print(f"El nuevo límite es {nuevo_limite}")
        break