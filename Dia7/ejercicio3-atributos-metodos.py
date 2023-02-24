class Alarma:
    def __init__(self):
        pass

    def postergar(self,cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")

alarm = Alarma()
alarm.postergar(25)