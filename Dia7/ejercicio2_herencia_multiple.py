class Vertebrado:
    vertebrado = True


class Ave(Vertebrado):
    tiene_pico = True

    def poner_huevos(self):
        print("Poniendo huevos")


class Reptil(Vertebrado):
    venenoso = True


class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")

    def poner_huevos(self):
        print("Poniendo huevos")


class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")

    def amamantar(self):
        print("Amamantando crías")

class Ornitorrinco(Mamifero,Pez,Reptil,Ave):
    pass

x = Ornitorrinco()
x.poner_huevos()
print(x.tiene_pico)
print(x.vertebrado)
print(x.venenoso)
x.nadar()
x.caminar()
x.amamantar()