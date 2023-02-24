print("Bienvenid@ al sistema de calculo de comision de la avicola Villena: ")
nombre = input("Por favor ingrese su nombre: ")
kilos_vendidos = int(input("Cuantos kilos has vendido? "))
precio = 7.5
montoVendido = kilos_vendidos * precio
Comision = round((montoVendido * 25) / 100,2)
print(f"""Usted ha vendido S/ {montoVendido} por lo tanto,
le pagaremos un total de S/ {Comision}""")