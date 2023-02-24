texto = "Este es un texto de prueba de Jasef"
print(texto.count('a'))
print(texto.count('de'))
print(texto.startswith("Hola"))
print(type(texto.startswith("Hola")))
print(texto.isdigit())

texto = "abcd5"
print("se cambio a abcd5")
print(texto.isdigit())
print(texto.isnumeric())
texto = "09561237"

print("se cambio a 09561237")
print(type(texto))
print(texto.isdigit())
print(texto.isnumeric())


texto = "97"

print("se cambio a 97")
print(type(texto))
print(texto.isdecimal())

texto = "frAse dE Prueba"
print(texto.lower())
print(texto.upper())
print(texto.capitalize())
print(texto.islower())
print(texto.isupper())

