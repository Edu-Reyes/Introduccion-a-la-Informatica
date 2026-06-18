"Bienvenido al programa de promedio de notas"

def calcular_promedio():

    cantidad = int(input("Ingrese la cantidad de alumnos: "))

    while cantidad <= 0:
        print("Error. Debe ingresar una cantidad mayor a 0.")
        cantidad = int(input("Ingrese la cantidad de alumnos: "))

    suma = 0

    for i in range(cantidad):

        nota = float(input(f"Ingrese la nota del alumno {i + 1}: "))

        while nota < 0 or nota > 10:
            print("Error. La nota debe estar entre 0 y 10.")
            nota = float(input(f"Ingrese la nota del alumno {i + 1}: "))

        suma += nota

    promedio = suma / cantidad

    return promedio


print(f"El ptromedio final es {calcular_promedio()}")