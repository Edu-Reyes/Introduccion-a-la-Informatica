"BIenvenido al programa de calculo de salario mensual"

salario = float(input("Ingrese su salario mensual: "))
porcentaje = float(input("Ingrese el porcentaje de ahorro: "))
precio = float(input("Ingrese el precio del producto: "))

ahorro_mensual = salario * porcentaje / 100

meses = int(precio // ahorro_mensual)

if precio % ahorro_mensual != 0:
    meses += 1

print("Necesita", meses, "meses para comprar el producto")