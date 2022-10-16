lista = ["p","j","h","i"]

for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f"Letra {numero_letra}: {letra}")

lista = ['pablo', 'pedro', 'johana']

for nombre in lista:
    if nombre.startswith('p'):
        print(nombre)
    else:
        print("nombre que no comienza con l")

numeros = [1,2,3,4,5]
mi_valor= 0

for numero in numeros:
    mi_valor = mi_valor + numero
print(mi_valor)

palabra = "python"

for letra in palabra:
    print(letra)

dic = {"clave1":"a","clave2":"b","clave3":"c"}
for a,b in dic.items():
    print(a,b)

alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]
for alumno in alumnos_clase:
    print(f"hola {alumno}")

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0
for numero in lista_numeros:
    suma_numeros = suma_numeros + numero
print(suma_numeros)

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0


for numero in lista_numeros:
    numero = numero % 2
    if numero == 0:
        suma_pares = suma_pares + numero



