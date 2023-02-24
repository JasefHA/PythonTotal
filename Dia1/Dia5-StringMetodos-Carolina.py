texto = "Este es un texto de prueba de Jasef"
print(texto.count('e'))
print(texto.count('a'))
print(texto.count('s'))
print(texto.count('de'))
print(texto.count('texto'))
print(texto.find('Jasef'))
print(texto[14])
print(texto.startswith("Hola"))
print(type(texto.startswith("Hola")))

texto = "abcd5"
print("se cambio a abcd5")
print(type(texto))
print(texto.isdigit())
print(type(texto.isdigit()))
print(texto.isnumeric())
print(type(texto.isnumeric()))


texto = "123456"
print("se cambio a 123456")
print(type(texto))
print(texto.isdigit())
print(type(texto.isdigit()))
print(texto.isnumeric())
print(type(texto.isnumeric()))

texto = "estO es un TextO de Prueba"
print(texto.upper())
print(texto.lower())
print(texto.capitalize())
print(texto.isupper())
print(texto.islower())

texto = texto.replace("TextO","texto")
print(texto)

texto = texto.replace("estO","esto")
print(texto)

nombre= "Jasef"
apellido="Huachambe"
NombreCompleto=nombre+" "+apellido
print(NombreCompleto)
print(f"{nombre} {apellido}")

separador = ","
separador = separador.join(["Python", "C++", "Java", "Go"])
print(separador)
