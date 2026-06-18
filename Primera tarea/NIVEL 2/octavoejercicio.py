print("Bienvenido al programa que evalúa si un número es par o impar")

while True:
    numero = int(input("Ingrese un número: "))

    if numero % 2 == 0:
        print("Es par")
    else:
        print("Es impar")

    repetir = input("¿Usted desea continuar? (s por SI/ n por NO): ")

    if repetir == "n":
        break