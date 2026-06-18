print("Bienvenido al programa de si funciona o no una lámara")

funciona = input("¿La lámpara funciona? (s por SI/ n por NO): ")

if funciona == "s":
    print("La lámpara funciona correctamente")

else:
    conectada = input("¿Está conectada? (s por SI/ n por NO): ")

    if conectada == "n":
        print("Conecte la lámpara")

    else:
        foco = input("¿El foco no funciona? (s po SI/ n por NO): ")

        if foco == "s":
            print("Cambie el foco")
        else:
            print("Lleve para que se lo reparen")