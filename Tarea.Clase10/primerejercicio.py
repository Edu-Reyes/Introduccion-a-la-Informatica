"Bienvenido al programa sobre crear clase Persona"

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")


while True:
    nombre = input("Ingrese el nombre: ").strip()

    if nombre.replace(" ", " ").isalpha():
        break

    print("Error. Ingrese solo letras.")


while True:

    try:
        edad = int(input("Ingrese la edad: "))

        if edad > 0:
            break

        print("La edad debe ser mayor a 0.")

    except ValueError:
        print("Error. Ingrese un número.")


persona = Persona(nombre, edad)
persona.saludar()