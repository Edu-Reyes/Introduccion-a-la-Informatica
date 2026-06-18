"Bienvenido al programa de una carrera de ludo"
import random

def carrera_ludo():
    posiciones = 0
    lanzamientos = 0

    print("Bienvenido al juego del ludo")
    while posiciones < 24:

        input("Presione la tecla ENTER para tirar el dado")
        dado = random.randint(1,6)

        lanzamientos += 1
        posiciones += dado

        print(f"El lanzamiento {lanzamientos}, -DADO: {dado}")
        print(f"Las posiciones acumuladas es: {posiciones}")

    print(f"Felicidades, usted ganó la partda con un total de {lanzamientos} lanzamientos realizados")
    
carrera_ludo()