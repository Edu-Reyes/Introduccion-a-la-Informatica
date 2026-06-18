"Bienvenido al programa de calculo de pago final"

precio = float(input("Ingrese el precio del artículo: "))

precio_descuento = precio * 0.80
precio_final = precio_descuento * 1.21

print("Precio con descuento:", precio_descuento)
print("Precio final con IVA:", precio_final)