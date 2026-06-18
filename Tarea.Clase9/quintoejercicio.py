"Bienvenido al programa que realiza una estadística de un archivo"

with open("texto.Quintoejercicio.txt", "r", encoding="utf-8") as archivo:

    texto = archivo.read()

with open("texto.Quintoejercicio.txt", "r", encoding="utf-8") as archivo:

    lineas = archivo.readlines()

cantidad_lineas = len(lineas)

palabras = texto.split()
cantidad_palabras = len(palabras)

cantidad_caracteres = len(texto)

print(f"Cantidad de líneas: {cantidad_lineas}")
print(f"Cantidad de palabras: {cantidad_palabras}")
print(f"Cantidad de caracteres: {cantidad_caracteres}")