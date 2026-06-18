print("BInvenido al programa de cálculo de precio final")

precio = input("Ingrese el precio del producto: ")

while not precio.isdigit():
    print("Por favor, ingrese solo números")
    precio = input("Ingrese el precio del producto: ")

precio = int(precio)

descuento = precio * 0.20

precio_descuento = precio - descuento

iva = precio_descuento * 0.21

precio_final = precio_descuento + iva

print(f"El precio final es $ {precio_final} pesos")
