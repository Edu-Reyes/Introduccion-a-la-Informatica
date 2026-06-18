"Bienvenido al programa del calculador de notas"

class Estudiante:

    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas

    def obtener_promedio(self):
        return sum(self.notas) / len(self.notas)

    def aprobo(self):
        return self.obtener_promedio() >= 6


while True:
    nombre = input("Ingrese el nombre: ").strip()

    if nombre.replace(" ", "").isalpha():
        break

    print("Error. Ingrese solo letras.")


notas = []

for i in range(3):

    while True:

        try:
            nota = float(input(f"Ingrese la nota {i + 1}: "))

            if 0 <= nota <= 10:
                notas.append(nota)
                break

            print("La nota debe estar entre 0 y 10.")

        except ValueError:
            print("Error. Ingrese un número válido.")


alumno = Estudiante(nombre, notas)

print(f"Promedio: {alumno.obtener_promedio()}")

if alumno.aprobo():
    print("Muy bien, aprobó")
else:
    print("No aprobó")