"Bienvenido al programa de validación de mayúsculas"

def vocales_mayusculas(texto):

    texto = texto.replace("a", "A")
    texto = texto.replace("e", "E")
    texto = texto.replace("i", "I")
    texto = texto.replace("o", "O")
    texto = texto.replace("u", "U")

    return texto


while True:

    frase = input("Ingrese una frase: ").strip()

    if len(frase) > 0:
        break

    print("Debe ingresar una frase.")

print(vocales_mayusculas(frase))