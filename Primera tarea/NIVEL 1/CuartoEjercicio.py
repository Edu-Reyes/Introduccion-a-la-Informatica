print ("Bienvenidos al programa de conversión de moneda")

dolar= int(input("Ingrese los dólares a cambiar: "))
cotizacion= int(input("Ingrese la cotización actual: "))


while dolar >= 0:
    if dolar >= 0:
        break
    else:
        print("El valor no puede ser negatico, intente nuevamente")
        dolar= int(input("Ingrese los dólares a cambiar: "))

while cotizacion >= 0:
    if cotizacion >= 0:
        break
    else:
        print("El valor no puede ser negatico, intente nuevamente")
        cotizacion= int(input("Ingrese la cotización actual: "))


pesos = dolar * cotizacion

print(f"Usted recibirá segun la cotización actual ${pesos} pesos")



