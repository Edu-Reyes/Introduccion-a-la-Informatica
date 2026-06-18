"Bienvenido al programa que simula una cuenta de banco"

class Cuenta:

    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto

    def retirar(self, monto):
        if 0 < monto <= self.saldo:
            self.saldo -= monto
        else:
            print("Saldo insuficiente o no es válido.")


while True:
    titular = input("Titular: ").strip()

    if titular.replace(" ", "").isalpha():
        break

cuenta = Cuenta(titular)

while True:
    try:
        deposito = float(input("Depositar: "))
        if deposito > 0:
            cuenta.depositar(deposito)
            break
    except ValueError:
        print("Error.")

while True:
    try:
        retiro = float(input("Retirar: "))
        if retiro > 0:
            cuenta.retirar(retiro)
            break
    except ValueError:
        print("Error.")

print(f"Su saldo es de : ${cuenta.saldo} pesos")