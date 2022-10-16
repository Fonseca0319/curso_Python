
pies = [10,20,30,40]
metros = [p * 3.281 for p in pies]
print(metros)
print("\n")

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrados = [v **2 for v in valores]
print(valores_cuadrados)

temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(temperatura_fahrenheit - 32)*(5/9) for c in temperatura_fahrenheit]
print(grados_celsius)