"Bienvenido al programa sobre una agenda telefónica"

while True:

    nombre = input("Nombre: ").strip()

    telefono = input("Teléfono: ").strip()

    with open("agenda.Cuartoejercicio.txt", "a", encoding="utf-8") as archivo:

        archivo.write(nombre + "," + telefono + "\n")

    opcion = input("¿Quiere agregar otro contacto? SI/NO): ").lower()

    if opcion != "si":
        break

print("Contactos guardados:")

with open("agenda.Cuartoejercicio.txt", "r", encoding="utf-8") as archivo:

    lineas = archivo.readlines()

for linea in lineas:

    datos = linea.strip().split(",")

    print(f"Nombre: {datos[0]}, Teléfono: {datos[1]}")