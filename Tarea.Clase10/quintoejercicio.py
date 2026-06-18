"Bienvenido al programa de manejo de un ventilador"

class Ventilador:

    def __init__(self):
        self.encendido = False
        self.velocidad = 0

    def encender(self):
        self.encendido = True
        print("Ventilador encendido.")

    def apagar(self):
        self.encendido = False
        self.velocidad = 0
        print("Ventilador apagado.")

    def cambiar_velocidad(self, velocidad):

        if self.encendido:
            self.velocidad = velocidad
            print("Cambió de velocidad.")
        else:
            print("Primero debe encender el ventilador.")


ventilador = Ventilador()

while True:

    opcion = input(
        "1.Encender\n2.Apagar\n3.Cambiar velocidad\n4.Salir\nQue opción elige: "
    )

    if opcion == "1":
        ventilador.encender()

    elif opcion == "2":
        ventilador.apagar()

    elif opcion == "3":

        if ventilador.encendido:

            while True:

                try:
                    velocidad = int(input("Ingrese una velocidad (1 a 3): "))

                    if 1 <= velocidad <= 3:
                        ventilador.cambiar_velocidad(velocidad)
                        break

                    print("La velocidad debe ser entre 1 y 3.")

                except:
                    print("Ingrese un número válido.")
        else:
            print("El ventilador está apagado.")

    elif opcion == "4":
        break

    else:
        print("Opción inválida.")

    print(f"A la velocidad de nivel: {ventilador.velocidad}")