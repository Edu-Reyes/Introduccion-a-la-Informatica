print ("Bienvenido al programa de cálculo de salario semanal")

hora= input("Ingrese sus horas trabajadas: ")
pagoxhora = input("Ingrese el pago por hora: ")

while not hora.isdigit():

        print("Por favor, ingrese un valor numérico")
        hora= input("Ingrese sus horas trabajadas: ")

pagoxhora = input("Ingrese el pago por hora: ")

while not pagoxhora.isdigit():

        print("Por favor, ingrese un valor numérico")
        pagoxhora = input("Ingrese el pago por hora: ")

hora= int(hora)
pagoxhora= int(pagoxhora)

sueldo = hora*pagoxhora
print(f"Su sueldo semanal es de ${sueldo} pesos.")