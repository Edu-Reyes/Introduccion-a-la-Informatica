"Bienvenido al programa de grito de cvocales"

def grito_vocales():

    resultado = ""

    for letra in frase:

        if letra.lower() in "aeiou":
            resultado += letra.upper()
        else:
            resultado += letra

    return resultado


while True:

    frase = input("Ingrese una frase: ")

    if len(frase) > 0:
        break
    else:
        print("Debe ingresar una frase.")

print(grito_vocales())