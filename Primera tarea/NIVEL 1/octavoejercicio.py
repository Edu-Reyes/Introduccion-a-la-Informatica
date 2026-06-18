print("Bienvenido al programa para calcular un ahorro de cimpra")

salario = input("Ingrese su salario mensual: ")
porcentaje = input("Ingrese el porcentaje de ahorro: ")
producto = input("Ingrese el precio del producto: ")

if salario.isdigit() and porcentaje.isdigit() and producto.isdigit():
    salario = int(salario)
    porcentaje = int(porcentaje)
    producto = int(producto)

    ahorro = salario * (porcentaje / 100)

    meses = producto / ahorro

    print(f"Necesita {meses} meses para comprar el producto que quiere")

else:
    print("Por favor ingrese solo números")