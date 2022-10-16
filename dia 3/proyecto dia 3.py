texto = input("ingrese un texto cualquiera: ")
letras = []

texto = texto.lower()

letras.append(input("ingrese la primer letra: ").lower())
letras.append(input("ingrese la segunda letra: ").lower())
letras.append(input("ingrese la tercera letra: ").lower())

print("\n")
print("CANTIDAD DE LETRAS")

cantidad_letras1 = texto.count(letras[0])
cantidad_letras2= texto.count(letras[1])
cantidad_letras3= texto.count(letras[2])

print(f"Hemos encontra la letra '{letras[0]}' repetida {cantidad_letras1}")
print(f"Hemos encontra la letra '{letras[1]}' repetida {cantidad_letras2}")
print(f"Hemos encontra la letra '{letras[2]}' repetida {cantidad_letras3}")

print('\n')
print("CANTIDAD DE PALABRAS")
palabras = texto.split()
print(f"Hemos encontrado {len(palabras)} en tu texto")
print("\n")
print("PALABRA INICIAL Y FINAL")
letra_inicial = texto[0]
letra_final = texto [-1]
print(f"la letra inicial es: '{letra_inicial}' y la letra final es: '{letra_final}'")
print("\n")
print("TEXTO INVERTIDO")

palabras.reverse()
texto_invertido = " ".join(palabras)
print(f"si ordenamos tu texto al reves va a decir: '{texto_invertido}'")
print("\n")
print("BUSCANDO LA PALABRA python")

buscar_python = "python" in texto
dic = {True:"si", False:"no"}
print(f"la palabra python {dic[buscar_python]} se encuentra en el texto")
