import os
import pathlib
from pathlib import Path
from os import system,remove
from shutil import rmtree

def ElegirCategoria(base):
    contador = 0
    opcionCategoria = 0
    CategoriaElegida = ""
    system('cls')
    directorio = pathlib.Path(base)
    ficheros = [fichero.name for fichero in directorio.iterdir() if fichero.is_dir()]
    print("Elija la categoria")
    for subdirectorio in ficheros:
        contador += 1
        print(f"{contador}"+". "+f"{subdirectorio}")
    opcionCategoria = int(input("Que opcion elige? (ingrese el numero)"))
    contador = 0
    for subdirectorio in ficheros:
        contador += 1
        if (contador == opcionCategoria):
            CategoriaElegida = subdirectorio
        else:
            print("No se encontró la categoria elegida")
            #print(f"Usted eligio {CategoriaElegida}")

    return CategoriaElegida

def Mostrar_Recetas (Categoria,ruta_base):
    system('cls')
    ruta = Path(ruta_base,Categoria)
    contador = 0
    #archivo_r = "No se encontro la receta ingresada"

    for txt in (Path(ruta).glob("**/*.txt")):
        contador += 1
        print(f"{contador}.{txt.name[:-4]}")

    if (contador >0 ):
        print(f"Las recetas de {Categoria} son:")
        receta = int(input("Por favor elija una receta :"))

        contador = 0
        for txt in (Path(ruta).glob("**/*.txt")):
            contador += 1
            if (contador == receta):
                archivo = open(txt)
                print(archivo.read())

        archivo.close()
    else:
        print("No hay recetas disponibles para esta categoria")



def Crear_Receta (Categoria,ruta_base):
    system('cls')
    ruta = Path(ruta_base,Categoria)
    #print(f"Usted se encuentra posiciado en {ruta}")
    nombre_nueva_receta = input("Ingrese el nombre de la nueva receta: ")
    nueva_receta = open(ruta/f"{nombre_nueva_receta}.txt","w")
    CuerpoReceta = input("Escriba su receta : ")
    nueva_receta.write(CuerpoReceta)
    nueva_receta.close()

def Eliminar_Recetas (Categoria,ruta_base):
    system('cls')
    ruta = Path(ruta_base,Categoria)
    print (f"Las recetas de {Categoria} son:")
    contador = 0

    for txt in (Path(ruta).glob("**/*.txt")):
        contador += 1
        print(f"{contador}.{txt.name[:-4]}")

    receta = int(input("Por favor elija la receta a eliminar:"))

    contador = 0
    for txt in (Path(ruta).glob("**/*.txt")):
        contador += 1
        #print(txt)
        if(contador == receta):
            Confirmar = ""
            while(Confirmar.upper() != 'N' and Confirmar.upper() != 'Y'):
                Confirmar = input(f"Esta seguro de eliminar la receta {txt.name} (Y - N)?")
                if ((Confirmar.upper()) == "Y"):
                    RecetaEliminada = txt.name
                    remove(txt)
                    print(f"Se elimino la receta de {RecetaEliminada}")
                elif (Confirmar.upper() == "N"):
                    print("Se canceló el proceso")

def Eliminar_Categoria (Categoria,ruta_base):
    system('cls')
    ruta = Path(ruta_base,Categoria)
    rmtree(ruta)
    print (f"Se eliminó la categoria {ruta.name}")

def Crear_Categoria (ruta_base):
    system('cls')
    nueva_categoria = input("Ingrese el nombre de la nueva categoria")
    nueva_dir = ruta_base/f"{nueva_categoria}"
    nueva_dir.mkdir(parents=True,exist_ok=True)


def ObtenerCantidadRecetas():
    CantidadRecetas = 0
    for txt in Path(ruta_base).glob("**/*.txt"):
        CantidadRecetas += 1
    return CantidadRecetas

def Acciones(opcion,ruta_base):
    Categoria = ""
    if (opcion==1):
        Categoria = ElegirCategoria(ruta_base)
        Mostrar_Recetas(Categoria,ruta_base)

    if (opcion==2):
        Categoria = ElegirCategoria(ruta_base)
        Crear_Receta(Categoria,ruta_base)

    if (opcion==3):
        Crear_Categoria(ruta_base)

    if (opcion==4):
        Categoria = ElegirCategoria(ruta_base)
        Eliminar_Recetas(Categoria,ruta_base)

    if (opcion==5):
        Categoria = ElegirCategoria(ruta_base)
        Eliminar_Categoria(Categoria,ruta_base)


ruta_base = Path(Path.home()/"Recetas")
cantidadRecetas = ObtenerCantidadRecetas()
opcion = 0
continuar = True

print("Bienvenido al Recetario python")
print(f"Las recetas se encuentran en {ruta_base}")

print((f"Tenemos un total de {cantidadRecetas} recetas"))
input("Presione enter para continuar")

system('cls')



while((opcion<1 or opcion >6) or (continuar == True)):
    print("[1] Leer Receta")
    print("[2] Crear Receta")
    print("[3] Crear Categoría")
    print("[4] Eliminar Receta")
    print("[5] Eliminar Categoría")
    print("[6] Finalizar Programa")

    opcion = int(input("Por favor elegir una opción:"))

    if(opcion<1 or opcion >6):
        print("Por favor Ingrese un a opción Válida")
        input("Presione enter para volver a intentar")
        system('cls')

    if (opcion == 6):
        continuar = False
        print("Gracias por utilizar nuestro recetario")
    else:
        Acciones(opcion,ruta_base)
        input("Presione cualquier tecla para continuar")
        system('cls')





