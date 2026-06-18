"Bienvenido al programa sobre un auto y los KM recorridos"

class Auto:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.kilometraje = 0

    def conducir(self, distancia):
        self.kilometraje += distancia

    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Kilometraje: {self.kilometraje} km")


marca = input("Ingrese la marca: ")
modelo = input("Ingrese el modelo: ")

auto = Auto(marca, modelo)

while True:

    opcion = input(
        "\n1.Conducir\n2.Ver información\n3.Salir\nQué opción elige: "
    )

    if opcion == "1":

        while True:

            try:
                distancia = float(input("Ingrese los kilómetros recorridos: "))

                if distancia >= 0:
                    auto.conducir(distancia)
                    break

                print("No puede ser negativa.")

            except:
                print("Ingrese un número válido.")

    elif opcion == "2":
        auto.mostrar_info()

    elif opcion == "3":
        print("Gracias por usar el programa")
        break

    else:
        print("Opción inválida.")