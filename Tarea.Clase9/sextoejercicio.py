"Bienvenido al programa que realiza un sistema de notas"

while True:
    while True:
        alumno = input("Nombre del alumno: ").strip()

        if alumno.replace(" ", "").isalpha():
            break
        print("Error. Ingrese solo letras.")

    while True:
        try:
            nota = float(input("Nota (0-10): "))

            if 0 <= nota <= 10:
                break

            print("La nota debe estar entre 0 y 10.")

        except ValueError:
            print("Error. Ingrese un número positivo.")

    # GUARDAR EN ARCHIVO
    with open("notas.Sextoejercicio.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{alumno},{nota}\n")

    opcion = input("¿Quiere agregar otro alumno? (SI/NO): ").lower()

    if opcion != "si":
        break


# LECTURA DEL ARCHIVO
with open("notas.Sextoejercicio.txt", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()

suma = 0
mayor = -1
menor = 11
cantidad = 0
aprobados = []

for linea in lineas:

    nombre, nota = linea.strip().split(",")
    nota = float(nota)

    suma += nota
    cantidad += 1

    if nota > mayor:
        mayor = nota

    if nota < menor:
        menor = nota

    if nota >= 6:
        aprobados.append(nombre)

if cantidad > 0:
    promedio = suma / cantidad
else:
    promedio = 0

print(f"El promedio del alumnado es: {promedio}")