nombre = input("ingrese su nombre: ")
ventas = input(" ingrese el total de sus ventas: ")

ventas = float(ventas)
porcentaje_ganado = ventas * 13 / 100
porcentaje_ganado = round(porcentaje_ganado)
print(f"su ventas del año fueron {ventas} y su porcentaje de ganancia fue {porcentaje_ganado}")