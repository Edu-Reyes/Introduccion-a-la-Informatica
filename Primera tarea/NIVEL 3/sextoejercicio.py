print("BIenvenido al sistema que imprime los meses que elegis")

meses = (
    "Enero", "Febrero", "Marzo", "Abril",
    "Mayo", "Junio", "Julio", "Agosto",
    "Septiembre", "Octubre", "Noviembre", "Diciembre"
)

while True:
    numero = int(input("Ingrese un número del 1 al 12: "))

    if numero >= 1 and numero <= 12:
        print(f"El mes es: {meses[numero - 1]}")
        break
    else:
        print("Número inválido")