"Bienvendo al programa de calculo de vuelto"

precio = float(input("Ingrese el precio del producto: "))
abonado = float(input("Ingrese el importe abonado: "))

if abonado < precio:
    print("Dinero insuficiente.")
else:
    vuelto = abonado - precio
    print("Vuelto: $", vuelto, " pesos")