"Bienvenido al programa que calcula la nota promedio"

cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))

while cantidad_alumnos <= 0:
    print("La cantidad debe ser mayor que cero.")
    cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))

suma_notas = 0
i = 1

while i <= cantidad_alumnos:

    nota = float(input("Ingrese la nota del alumno", i,": "))

    while nota < 0 or nota > 10:
        print("La nota debe estar entre 0 y 10.")
        nota = float(input("Ingrese la nota del alumno", i,": "))

    suma_notas += nota
    i += 1

promedio = suma_notas / cantidad_alumnos

print("\nPromedio del curso:", promedio)