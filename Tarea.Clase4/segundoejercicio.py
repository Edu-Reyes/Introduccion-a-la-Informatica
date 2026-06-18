print("Bienvenido al programa de cálculo de compra")

total = 0

while True:
    entrada = input("Ingrese el precio del producto (0 para finalizar): ")

    if entrada.isdigit():
        precio = float(entrada)

        if precio == 0:
            break

        total += precio

    else:
        print("Ingrese un número entero positivo).")

print("Resumen de la compra")
print("Total a pagar: $", total, "pesos")