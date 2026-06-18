"Bienvenido al programa sobre registro de alumnos"

with open("alumnos.txt", "w", encoding="utf-8") as archivo:

    for i in range(5):

        nombre = input(f"Ingrese el alumno {i + 1}: ").strip()

        archivo.write(nombre + "\n")

with open("alumnos.txt", "r", encoding="utf-8") as archivo:

    lineas = archivo.readlines()

print("Lista de alumnos:")

for numero, alumno in enumerate(lineas, start=1):

    print(numero, "-", alumno.strip())

print(f"La cantidad de alumnos: {len(lineas)}")
