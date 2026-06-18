"Bienvenido al programa sobre el desafio de empleados"

cantidad = input("Ingrese la cantidad de empleados: ")

while not cantidad.isdigit() or int(cantidad) <= 0:
    print("La cantidad no es válido.Ingrese números")
    cantidad = input("Ingrese la cantidad de empleados: ")

cantidad = int(cantidad)

total_salarios = 0
mas_200000 = 0
menos_50000_cat3 = 0
mayor_sueldo = None
legajo_mayor = None
sueldo_mas_bajo = None

total_cat1 = 0
total_cat2 = 0
total_cat3 = 0

for i in range(cantidad):

    print("Empleado", i + 1)

    legajo = input("Legajo: ")

    while not legajo.isdigit():
        print("Legajo inválido.")
        legajo = input("Legajo: ")

    legajo = int(legajo)

    categoria = input("Categoría (1, 2 o 3): ")

    while categoria not in ["1", "2", "3"]:
        print("La cantidad no es válido.Ingrese números")
        categoria = input("Categoría (1, 2 o 3): ")

    categoria = int(categoria)

    sueldo = input("Sueldo: ")

    while not sueldo.isdigit():
        print("Sueldo inválido. Ingrese números")
        sueldo = input("Sueldo: ")

    sueldo = int(sueldo)

    total_salarios += sueldo

    if sueldo > 200000:
        mas_200000 += 1

    if sueldo < 50000 and categoria == 3:
        menos_50000_cat3 += 1

    if mayor_sueldo is None or sueldo > mayor_sueldo:
        mayor_sueldo = sueldo
        legajo_mayor = legajo

    if sueldo_mas_bajo is None or sueldo < sueldo_mas_bajo:
        sueldo_mas_bajo = sueldo

    if categoria == 1:
        total_cat1 += sueldo
    elif categoria == 2:
        total_cat2 += sueldo
    else:
        total_cat3 += sueldo

promedio = total_salarios / cantidad

print("Total salarios:", total_salarios)
print("Empleados que ganan más de $200000 pesos:", mas_200000)
print("Empleados categoría 3 que ganan menos de $50000 pesos:", menos_50000_cat3)
print("Legajo del empleado que más gana:", legajo_mayor)
print("El sueldo más bajo: $", sueldo_mas_bajo, " pesos")
print("Total de la categoría 1: $", total_cat1, " pesos")
print("Total de la categoría 2: $", total_cat2, " pesos")
print("Total de la categoría 3:$", total_cat3, " pesos")
print("El salario promedio es : $", promedio, " pesos")