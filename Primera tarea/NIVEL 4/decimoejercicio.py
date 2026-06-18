"Bienvendido al programa de busqueda de anagramas"

def son_anagramas():

    return sorted(palabra1.lower()) == sorted(palabra2.lower())


while True:

    palabra1 = input("Ingrese la primera palabra: ")

    if not palabra1.isalpha():
        print("Ingrese solo letras.")
        continue

    palabra2 = input("Ingrese la segunda palabra: ")

    if not palabra2.isalpha():
        print("Ingrese solo letras.")
        continue

    if son_anagramas():
        print("Son anagramas")
        break
    else:
        print("No son anagramas, intente otra vez.")