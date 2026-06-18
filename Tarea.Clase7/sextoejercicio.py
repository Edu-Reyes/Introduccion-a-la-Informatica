"Bienvenido al programa sobre verificación de anagramas"

def son_anagramas(p1, p2):

    p1 = p1.lower()
    p2 = p2.lower()

    if len(p1) != len(p2):
        return False

    return sorted(p1) == sorted(p2)


while True:

    palabra1 = input("Ingrese la primera palabra: ").strip()

    if palabra1.isalpha():
        break

    print("Por favor, ingrese letras.")

while True:

    palabra2 = input("Ingrese la segunda palabra: ").strip()

    if palabra2.isalpha():
        break

    print("Por favor, ingrese letras.")

if son_anagramas(palabra1, palabra2):
    print("Son anagramas.")
else:
    print("No son anagramas.")