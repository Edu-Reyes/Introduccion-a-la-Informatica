print("Bienvenido al programa para calcular el áea de un triángulo")

base = input("Ingrese la base: ")

while not base.isdigit():
    print("Por favor ingrese solo números")
    base = input("Ingrese la base: ")

altura = input("Ingrese la altura: ")

while not altura.isdigit():
    print("Por favor ingrese solo números")
    altura = input("Ingrese la altura: ")


base = int(base)
altura = int(altura)

area = (base * altura) / 2

print(f"El área del triángulo es {area} ")