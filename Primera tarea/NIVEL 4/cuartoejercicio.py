"Bienvenido al programa de informes de Recursos HUmanos"

def informe_rrhh():

    cantidad = int(input("Ingrese la cantidad de empleados: "))

    while cantidad <= 0:
        print("Error, ingrese al menos un empleado.")
        cantidad = int(input("Cantidad de empleados: "))

    total_sueldo = 0
    mayor_sueldo = 0
    mayor_ganancia = ""

    for i in range(cantidad):
        print(f"Empleado {i + 1}")

        legajo = input("Legajo del empleado: ")
        categoria = input("Categoría del empleado: ")

        sueldo = float(input(f"Ingrese sueldo del empleado {i + 1}: "))

        while sueldo <= 0:
            print("Sueldo inválido.")
            sueldo = float(input(f"Ingrese sueldo del empleado {i + 1}: "))

        total_sueldo += sueldo

        if sueldo > mayor_sueldo:
            mayor_sueldo = sueldo
            mayor_ganancia = legajo

    promedio = total_sueldo / cantidad

    print(f"El rotal de pago a empleados: ${total_sueldo} pesos")
    print(f"El promedio de sueldos: ${promedio} pesos")
    print(f"El mayor sueldo registrado es del legajo {mayor_ganancia} con ${mayor_sueldo} pesos")

informe_rrhh()