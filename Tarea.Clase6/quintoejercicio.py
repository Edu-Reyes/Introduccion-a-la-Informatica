"Bienvenido al programa sobre el desafío de encriptación"

mensaje = input("Ingrese un mensaje: ")

fase1 = ""
grupo = ""

for letra in mensaje:

    if letra.lower() not in "aeiou" and letra.isalpha():
        grupo = letra + grupo
    else:
        fase1 += grupo
        grupo = ""
        fase1 += letra

fase1 += grupo

print("Fase 1:", fase1)

fase2 = ""

i = 0
j = len(fase1) - 1

while i <= j:

    fase2 += fase1[i]

    if i != j:
        fase2 += fase1[j]

    i += 1
    j -= 1

print("Fase 2:", fase2)