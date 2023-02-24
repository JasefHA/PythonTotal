import os
class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self,nombre,apellido,nrocuenta,balance):
        super().__init__(nombre,apellido)
        self.nrocuenta = nrocuenta
        self.balance = balance

    def __str__(self):
        return f"El cliente se llama {self.nombre} {self.apellido} \nSu cuenta es y tiene un balance de {self.balance}"

    def depositar(self):
        monto_deposito = int(input("Ingrese el monto a depositar: "))
        if(monto_deposito<=0):
            print("No se puede depositar 0 soles, ni valores negativos")
        else:
            self.balance = self.balance + monto_deposito
        print(f"Usted ha depositado S/{monto_deposito}\nSu nuevo balance es S/{self.balance}")


    def retirar(self):
        monto_retiro = int(input("Por favor ingrese el monto a retirar: "))
        if(monto_retiro > self.balance):
            print("El monto ingresado excede el balance de la cuenta")
        elif(monto_retiro <= 0):
            print("No se puede retirar 0 soles, ni valores negativos")
        else:
            self.balance = self.balance - monto_retiro
            print(f"Usted ha retirado S/{monto_retiro}, el saldo restante en su cuenta es S/{self.balance}")

Jareth = Cliente("Jareth","Huachambe",145454545,111111111)
Ejecucion = True
Opcion = 0
while(Ejecucion):
    print("""Bienvenido al cajero Python
    Por favor elija una opción:
    1. Depositar
    2. Retirar
    3. Salir
    """)
    Opcion = int(input("Por favor eliga una opción: "))
    if(Opcion <1 or Opcion >3):
        print("Por favor ingrese una opción valida")
    if(Opcion==3):
        print("Usted ha salido con éxito")
        Ejecucion = False
    if(Opcion==1):
        Jareth.depositar()
    if(Opcion==2):
        Jareth.retirar()
    input("Presione cualquier tecla para continuar...")
    os.system('cls')
