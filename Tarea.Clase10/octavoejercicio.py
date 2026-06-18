"Bienvenido al programa sobre una calculadora básica"

class Calculadora:

    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):

        if b != 0:
            return a / b

        return "No se puede dividir por cero."


calc = Calculadora()

while True:

    opcion = input(
        "\n1.Sumar\n2.Restar\n3.Multiplicar\n4.Dividir\n5.Salir\nQué opción elige: "
    )

    if opcion in ["1", "2", "3", "4"]:

        while True:

            try:
                a = float(input("Primer número: "))
                b = float(input("Segundo número: "))
                break

            except:
                print("Ingrese números válidos.")

        if opcion == "1":
            print("El resultado es:", calc.sumar(a, b))

        elif opcion == "2":
            print("El resultado es:", calc.restar(a, b))

        elif opcion == "3":
            print("El resultado es:", calc.multiplicar(a, b))

        elif opcion == "4":
            print("El resultado es:", calc.dividir(a, b))

    elif opcion == "5":
        print("Gracias por usar el programa")
        break

    else:
        print("Opción inválida.")