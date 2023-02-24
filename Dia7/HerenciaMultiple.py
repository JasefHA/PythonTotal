class Padre:
    def Hablar(self):
        print("Hola")

class Madre:
    def Reir(self):
        print("jaja")

    def Hablar(self):
        print("Que tal?")

class Hijo(Padre,Madre):
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()
mi_nieto.Hablar()
mi_nieto.Reir()