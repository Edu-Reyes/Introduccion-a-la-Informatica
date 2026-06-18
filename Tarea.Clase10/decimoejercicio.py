"Bienvenido al programa que hace una gestión de un changuito"

class Changuito:

    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print("Producto agregado.")

    def mostrar_changuito(self):

        if len(self.productos) == 0:
            print("El changuito está vacío.")

        else:
            print("\nProductos en el changuito:")

            for producto in self.productos:
                print(producto)


changuito = Changuito()

while True:

    opcion = input(
        "\n1.Agregar un producto\n2.Ver changuito\n3.Salir\nQue opción elige: "
    )

    if opcion == "1":

        while True:

            producto = input("Ingrese el producto: ").strip()

            if producto != "":
                changuito.agregar_producto(producto)
                break

            print("Tiene que agregar un producto, no puede estar vacío.")

    elif opcion == "2":
        changuito.mostrar_changuito()

    elif opcion == "3":
        print("Gracias por usar el programa")
        break
    else:
        print("Opción inválida.")