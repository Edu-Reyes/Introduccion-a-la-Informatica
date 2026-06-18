"Bienvenido al programa de estadistica de temperatura"

temperaturas = []

def minimo():
    return min(temperaturas)

def maximo():
    return max(temperaturas)

def promedio():
    return sum(temperaturas) / len(temperaturas)

def bajo_cero():
    contador = 0

    for temperatura in temperaturas:
        if temperatura < 0:
            contador += 1

    return contador

while True:
    try:
        cantidad = int(input("Ingrese la cantidad de días: "))

        if cantidad > 0:
            break

        print("Debe ingresar un número mayor a 0.")

    except:
        print("Ingrese un número váilido.")

for i in range(cantidad):

    while True:
        try:
            temperatura = float(input(f"Temperatura del día {i+1}: "))
            temperaturas.append(temperatura)
            break

        except:
            print("Ingrese una temperatura válida.")

print(f"la mínima temperatura es: {minimo()}")
print(f"La máxima temeratura es: {maximo()}")
print(f"El promedio de las temperauras ingresadas es: {promedio()}")
print(f"Lo días bajo cero son: {bajo_cero()}")