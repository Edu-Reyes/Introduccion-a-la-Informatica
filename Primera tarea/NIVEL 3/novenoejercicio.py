print("Bienvenido al sistema que analiza el valor acumulativo de un alqulesr")

monto = float(input("Ingrese el monto inicial: "))
meses = int(input("Ingrese la cantidad de meses: "))
incremento = float(input("Ingrese el porcentaje de aumento: "))

for i in range(1, meses + 1):
    print(f"En el Mes {i} será de ${round(monto, 2)} pesos")
    monto = monto + (monto * incremento / 100)