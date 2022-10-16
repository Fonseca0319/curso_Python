monedas = 5
while monedas >0:
    print(f"tengo {monedas} monedas ")
    monedas -= 1

print("\n")

respuesta = "s"

while respuesta == "s":
    respuesta = input("quieres seguir? (s/n)")
else:
    print("gracias")

print("\n")

nombre = input("cual es tu nombre: ")

for letra in nombre:
    if letra == "d":
        break
    print(letra)

print("\n")

numero = 10
while numero >0:
    numero -= 1
    print(f"numero: {numero} ")