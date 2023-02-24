class Pajaro:
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print(f"pio, mi color es {self.color}")
    def volar(self,metros):
        print(f"El pajaro ha volado {metros} metros")


##clases creadas para los ejercicios de udemy
class Casa:
    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos

class Cubo:
    def __init__(self,color):
        self.caras = 6
        self.color = color

#cubo_rojo = Cubo("rojo")

mi_pajaro = Pajaro('Azul','Paloma')
#casa_blanca = Casa("blanco","4")

#print(f"Mi pajaro es una {mi_pajaro.especie} y es de color {mi_pajaro.color}")

mi_pajaro.piar()
mi_pajaro.volar(15)