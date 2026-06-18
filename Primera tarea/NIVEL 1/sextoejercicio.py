print("Bienvenidos al programa de conversión de kilos a onzas")

kilos= input("Ingrese los kilos a convertir: ")

while not kilos.isdigit():

    print("Por favor, ingrese un valor numérico")
    kilos= input("Ingrese los kilos a convertir: ")

kilos = int(kilos)

onzas= kilos* 35.274

print(f"Los kilos ingresados equivalen a {onzas} onzas")
