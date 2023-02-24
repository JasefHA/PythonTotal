class Pajaro:
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print(f"pio, mi color es {self.color}")
    def volar(self,metros):
        print(f"El pajaro ha volado {metros} metros")
        self.piar()

    def pintar_netro(self):
        self.color = 'negro'
        print(f"Mi nuevo color es {self.color}")

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad}")
        cls.alas = False

    @staticmethod
    def mirar():
        print("El pago ha mirado")


#piolin = Pajaro('amarillo','canario')

#piolin.piar()
#piolin.volar(50)
#piolin.pintar_netro()
Pajaro.poner_huevos(100)
print(Pajaro.alas)
Pajaro.mirar()







