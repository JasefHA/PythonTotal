print("Bienvenido al sistema de calculo de comision de la avícola Villena")
nombre = input("Por favor ingrese su nombre: ")
cantidad = int(input("Por favor ingrese la cantidad de pollos vendidos: "))
precio = 19
MontoVendido = cantidad * precio
Comision = MontoVendido * 0.25
print(f"""Usted vendió el valor de S/{MontoVendido} 
por lo tanto le corresponde una comisión de S/{Comision}
""")
