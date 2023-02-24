#numero_uno = int(input("Por favor ingrese el primero numero: "))
#numero_dos = int(input("Por favor ingrese el segundo numero: "))
#suma = numero_uno + numero_dos
#division = numero_uno / numero_dos
#print(type(numero_uno))
#print(type(numero_dos))
#print(division)

#condicion = (3>5)
#print(condicion)
#print(type(condicion))

#tipos de datos
#texto = string
#numeros --> int -- entero (numeros sin decimales) // float (decimales)
#booleanos --> True (verdadero) // False (falso)
#listas
#tuplas
#sets
#diccionarios

numero_uno = int(input("Por favor ingrese el primer número: "))
numero_dos = int(input("Por favor ingrese el segundo número: "))

suma = numero_uno+ numero_dos
resta = numero_uno - numero_dos
multiplicacion = numero_uno * numero_dos
division = numero_uno / numero_dos
division_al_piso = numero_uno // numero_dos
resto = numero_uno % numero_dos
potencia = numero_uno ** numero_dos
raiz_cuadrada = numero_uno **0.5


print(f"La suma es: {suma}\nLa resta es: {resta}\nLa multiplicacion es: {multiplicacion}\n"
      f"La division es: {division}\nLa potencia es: {potencia}\n"
      f"El division al piso al piso es: {division_al_piso}\n"
      f"El resto al piso es: {resto}\n"
      f"La raiz_cuadrada al piso es: {raiz_cuadrada}\n"
)