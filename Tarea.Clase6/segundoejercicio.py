"Bienvenido al programa de mostrar un mes según el número"

meses = (
    "Enero", "Febrero", "Marzo", "Abril",
    "Mayo", "Junio", "Julio", "Agosto",
    "Septiembre", "Octubre", "Noviembre", "Diciembre"
)

while True:
    try:
        numero = int(input("Ingrese un número del 1 al 12: "))

        if 1 <= numero <= 12:
            break

        print("Error. Debe ingresar un número entre 1 y 12.")

    except ValueError:
        print("Error. Debe ingresar un número.")

print("El mes correspondiente es:", meses[numero - 1])