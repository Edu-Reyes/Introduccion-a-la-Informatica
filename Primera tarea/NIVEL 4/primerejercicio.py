"Bienvenido al sistema de registro de alumnos"

def registro_alumnos():

    total=0


    while True:
        
        print("Ingrese un nombre para registrar. Cuando haya finalizado en los registros, escriba FIN")
        nombre= input(("Alumno a registrar: "))

        if nombre.upper()== "FIN" and nombre.isalpha():
            break
        elif nombre =="":
            print("Por favor, ingrese un nombre.")
        else:
            print(f"Bienvenido {nombre}")

            total +=1

    print(f"Ell total de alumnos preentes es {total}")

registro_alumnos() 