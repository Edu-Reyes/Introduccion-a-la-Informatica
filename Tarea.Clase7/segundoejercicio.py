"Bienvenido al programa sobre validación de pnavocálicas"

def es_panvocalica(palabra):

    palabra = palabra.lower()

    return (
        palabra.find("a") != -1 and palabra.find("e") != -1 and palabra.find("i") != -1 and palabra.find("o") != -1 and palabra.find("u") != -1)


while True:

    palabra = input("Ingrese una palabra: ").strip()

    if palabra.isalpha():
        break

    print("Error. Ingrese solamente letras.")

if es_panvocalica(palabra):
    print("Es panvocálica.")
else:
    print("No es panvocálica.")