"Bienvenido al programa que busca una palabra"

contador = 0

with open("palabra.Segundoejercicio.txt", "r", encoding="utf-8") as archivo:

    lineas = archivo.readlines()

for linea in lineas:

    if "don" in linea.lower():

        contador += linea.lower().count("don")

print(f"La palabra DON aparece {contador} veces")