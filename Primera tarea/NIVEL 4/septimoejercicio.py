"Bienvenido al programa de validación de contraseñas"

def validar_contraseña():

    mayusculas = 0
    minusculas = 0
    numeros = 0

    for caracter in clave:

        if caracter.isupper():
            mayusculas += 1

        elif caracter.islower():
            minusculas += 1

        elif caracter.isdigit():
            numeros += 1

    if (len(clave) >= 8 and numeros >= 2 and mayusculas >= 1 and minusculas >= 1):
        return True
    else:
        return False


while True:

    clave = input("Por favor ingrese una contraseña: ")

    if validar_contraseña():
        print("Contraseña válida.")
        break

    print("Contraseña inválida.")