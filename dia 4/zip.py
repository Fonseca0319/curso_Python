nombres = ["johana","pedro","kelly"]
edades = [26,29,30]
mes_nacimineto = ["febreo","marzo","julio"]
combinados = list(zip(nombres,edades,mes_nacimineto))
print(combinados)

for nombre,edad,mes in combinados:
    print(f"{nombre} tiene {edad} años y nacio en el mes de {mes}")

print("\n")

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
combinados = list(zip(capitales,paises))

for capital,pais in combinados:
    print(f"la capital de {capital} es {pais}")