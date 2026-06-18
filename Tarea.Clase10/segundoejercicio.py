"Bienvenido al programa de rectángulo matemático"

class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)


while True:

    try:
        base = float(input("Ingrese la base: "))

        if base > 0:
            break

        print("La base debe ser positiva.")

    except:
        print("Error. Ingrese un número.")


while True:

    try:
        altura = float(input("Ingrese la altura: "))

        if altura > 0:
            break

        print("La altura debe ser positiva.")

    except ValueError:
        print("Error. Ingrese un número.")


rectangulo = Rectangulo(base, altura)

print(f"El área es: {rectangulo.calcular_area()}")
print(f"El perímetro es: {rectangulo.calcular_perimetro()}")