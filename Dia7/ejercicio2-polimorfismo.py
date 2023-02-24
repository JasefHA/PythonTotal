class Mago():
    def atacar(self):
        print("Ataque mágico")


class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")


class Samurai():
    def atacar(self):
        print("Ataque con katana")


Gandalf = Mago()
Arrow = Arquero()
Ichigo = Samurai()

personajes = [Arrow, Gandalf, Ichigo]

for x in personajes:
    x.atacar()