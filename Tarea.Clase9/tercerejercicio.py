"Bienvenido al programa de prueba de SEEK()"

with open("datos.Tercerejercicio.txt", "r", encoding="utf-8") as archivo:

    primera_linea = archivo.readline()

    print("Primera línea:")
    print(primera_linea)

    resto = archivo.read()

    print("EL RESTO:")
    print(resto)

    archivo.seek(0)

    completo = archivo.read()

    print("EL ARCHIVO COMPLETO:")
    print(completo)