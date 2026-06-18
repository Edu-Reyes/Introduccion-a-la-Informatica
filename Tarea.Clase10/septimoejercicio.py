"Bienvenido al programa sobre un celular y su bateria"

class Celular:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.bateria = 100

    def hacer_llamada(self, minutos):

        if minutos <= self.bateria:
            self.bateria -= minutos
            print("OK, llamada realizada.")
        else:
            print("No tiene más batería.")

    def cargar(self):
        self.bateria = 100
        print("Celu cargado al 100%.")

    def mostrar_estado(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Batería: {self.bateria}%")


marca = input("Ingrese la marca: ")
modelo = input("Ingrese el modelo: ")

celular = Celular(marca, modelo)

while True:

    opcion = input(
        "\n1.Hacer llamada\n2.Cargar batería\n3.Ver estado\n4.Salir\nQué opción elige: "
    )

    if opcion == "1":

        while True:

            try:
                minutos = int(input("Ingrese minutos que dura la llamada: "))

                if minutos > 0:
                    celular.hacer_llamada(minutos)
                    break

                print("Debe ser mayor que 0.")

            except:
                print("Ingrese un número válido.")

    elif opcion == "2":
        celular.cargar()

    elif opcion == "3":
        celular.mostrar_estado()

    elif opcion == "4":
        break

    else:
        print("Opción inválida.")