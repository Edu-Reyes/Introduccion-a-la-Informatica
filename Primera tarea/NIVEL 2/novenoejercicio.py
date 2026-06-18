print("Bienvendo al programa que analiza si unnegocio tuvo pérdida o ganancia")

while True:
    ingresos = float(input("Ingrese los ingresos: "))
    costos = float(input("Ingrese los costos: "))

    if ingresos < 0 or costos < 0:
        print("Valores inválidos")
    else:
        if ingresos >= costos:
            ganancia = ingresos - costos
            print(f"La ganancia es de ${ganancia} pesos")
        else:
            perdida = costos - ingresos
            print(f"La pérdida es de ${perdida} pesos")

        break