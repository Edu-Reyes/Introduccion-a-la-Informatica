"BIenvenido al programa de detección de panvocálicas"

def es_panvocalica():

    if ("a" in palabra and "e" in palabra and "i" in palabra and "o" in palabra and "u" in palabra):
        return True
    else:
        return False


while True:

    palabra = input("Ingrese una palabra: ").lower()

    if palabra.isalpha():
        break
    else:
        print("Ingrese solo letras.")

if es_panvocalica():
    print("La palabra es panvocálica.")
else:
    print("La palabra no es panvocálica.")