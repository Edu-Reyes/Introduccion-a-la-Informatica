"Bienvenido al programa de validación de contraseña"

def validar_password(password):

    if len(password) < 8:
        return False

    numeros = 0
    mayusculas = 0
    minusculas = 0

    for caracter in password:

        if caracter.isnumeric():
            numeros += 1

        elif caracter.isalpha():

            if caracter == caracter.upper():
                mayusculas += 1

            if caracter == caracter.lower():
                minusculas += 1

    return numeros >= 2 and mayusculas >= 1 and minusculas >= 1


while True:

    password = input("Ingrese una contraseña: ")

    if validar_password(password):
        print("Contraseña válida.")
        break

    print("Contraseña inválida.")
    print("Debe tener:")
    print("- Mínimo 8 caracteres")
    print("- Al menos 2 números")
    print("- Al menos 1 mayúscula")
    print("- Al menos 1 minúscula")