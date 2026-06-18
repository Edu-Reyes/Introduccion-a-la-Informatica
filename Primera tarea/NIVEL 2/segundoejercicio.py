print( "Bienvenido al programa de validaci´n de velto")

while True:
    precio = float(input("Ingrese el precio del producto: "))
    abonado = float(input("Ingrese el monto abonado: "))

    if precio <= 0 or abonado <= 0:
        print("Ingreso mal los datos")
    elif abonado < precio:
        print("Monto insuficiente")
    else:
        vuelto = abonado - precio
        print(f"El vuelto es ${vuelto} pesos")
        break