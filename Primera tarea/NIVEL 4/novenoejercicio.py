"Bienvenido al programa de analisis de órden alfbético"

def esta_ordenada():

    ordenada = True

    for i in range(len(palabra) - 1):

        if palabra[i] > palabra[i + 1]:
            ordenada = False

    return ordenada


while True:

    palabra = input("Ingrese una palabra: ").lower()

    if not palabra.isalpha():
        print("Tiene que ingresar solo letras.")
    elif esta_ordenada():
        print("Las letras están ordenadas alfabéticamente.")
        break
    else:
        print("Las letras no están ordenadas alfabéticamente. Intente de nuevo")