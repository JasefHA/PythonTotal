from pathlib import  Path, PureWindowsPath

ruta = Path(Path.home()/"Recetas")
print(ruta)

for txt in Path(ruta).glob("**/*.txt"):
    print(txt)
    archivo = open(txt)
    print(archivo.read())
#x = open(PureWindowsPath(Path(ruta)))
#base = Path.home()
#guia = Path(base,"Europa","España",Path("Barcelona","Sagrada_Familia.txt"))
#guia2 = guia.with_name("la_pedrera.txt")
#print(base)
#print(guia.parent.parent)
#print(guia2)

#guia = Path(Path.home(),"Europa")
#for txt in Path(guia).glob("**/*.txt"):
    #print(txt)


#guia2 = Path("Europa","España","Barcelona","Sagrada_Familia.txt")
#en_europa = guia2.relative_to(Path("Europa"))
#en_espania = guia2.relative_to(Path("Europa","España"))
#print(en_europa)
#print(en_espania)




