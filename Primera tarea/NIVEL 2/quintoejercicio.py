print("Bienvenido al programa que analiza si hay que cargar combustible")

while True:
    litros = float(input("Ingrese los litros del tanque: "))

    if litros < 0:
        print("Valor inválido")
    else:
        autonomia = litros * 12

        print(f"La autonomía es de {autonomia} km")

        if litros < 5:
            print("Urgente cargar combustible")
        break