numero_uno = int(input("Ingrese el primer numero: "))
numero_dos = int(input("Ingrese el segundo numero: "))

suma = numero_uno + numero_dos
resta = numero_uno - numero_dos
multiplicacion = numero_uno * numero_dos
potencia = numero_uno ** numero_dos
division = numero_uno / numero_dos
division_al_piso = numero_uno // numero_dos
resto = numero_uno % numero_dos
raiz_cuadrada = numero_uno ** 0.5
raiz_cubica = numero_uno ** (1/3)
raiz = numero_uno ** (1/numero_dos)

print(f"""La suma es {suma}
La resta es {resta}
La multiplicacion es {multiplicacion}
La potencia es {potencia}
La division es {division}
La division_al_piso es {division_al_piso}
La resto es {resto}
La raiz_cuadrada es {raiz_cuadrada}
La raiz_cubica es {raiz_cubica}
La raiz es {raiz}
""")