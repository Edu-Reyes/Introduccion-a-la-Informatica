print("Bienvenido al programa de ruta vs ciudad")

while True:
    litros = float(input("Ingrese litros: "))
    camino = input("Ingrese el tipo de camino (r por ruta/c por ciudad): ")

    if litros < 0:
        print("Litros inválidos")
    elif camino != "r" and camino != "c":
        print("Tipo de camino incorrecto")
    else:
        if camino == "r":
            autonomia = litros * 14
        else:
            autonomia = litros * 10

        print(f"La autonomía es de {autonomia} km")
        break