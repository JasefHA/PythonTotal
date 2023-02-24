def sobrescribir(archivo):
    x = open(archivo,'w')
    x.write("contenido eliminado")


def registro_error(archivo):
    x = open(archivo, 'a')
    x.write("se ha registrado un error de ejecución")