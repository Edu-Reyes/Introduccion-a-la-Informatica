print("Bienvenido al programa que evalúa el mayor de tres valores")

while True:
    num_1 = int(input("Ingrese el primer número: "))
    num_2 = int(input("Ingrese el segundo número: "))
    num_3 = int(input("Ingrese el tercer número: "))

    if num_1 == num_2 or num_1 == num_3 or num_2 == num_3:
        print("Los números deben ser diferentes")
    else:
        if num_1 > num_2 and num_1 > num_3:
            print(f"El mayor es el número {num_1}")
        elif num_2 > num_1 and num_2 > num_3:
            print(f"El mayor es el número {num_2}")
        else:
            print(f"El mayor es el número {num_3}")
        break