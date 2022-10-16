import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('case_time_series.csv', delimiter=',')
print(data)

Y = data.iloc[61:, 1].values  # confirmados diarios
R = data.iloc[61:, 3].values  # recuperados diarios
D = data.iloc[61:, 5].values  # difuntos diarios
X = data.iloc[61:, 0]  # fecha
plt.plot(X, Y)

plt.figure(figsize=(25, 8))

ax = plt.axes()
ax.grid(linewidth=0.4, color='#8f8f8f')  # CREAR UNA CUADRICULA A LO LARGO DEL GRAFICO

ax.set_facecolor("green")  # FONDO DEL COLOR DEL GRAFICO
ax.set_xlabel('\nDate', size=25, color='#4bb4f2')
ax.set_ylabel('Number of Confirmed Cases\n',
              size=25, color='#4bb4f2')

plt.xticks(rotation='vertical', size='20', color='white')  # MODIFICAR LAS FECHAS Y LA FUENTE DIARIA
plt.yticks(size=20, color='white')
plt.tick_params(size=20, color='white')

for i, j in zip(X, Y):
    ax.annotate(str(j), xy=(i, j + 100), color='white', size='13')

ax.annotate('Second Lockdown 15th April',
            xy=(15.2, 860),
            xytext=(19.9, 500),
            color='white',
            size='25',
            arrowprops=dict(color='white',
                            linewidth=0.025))  # FUNCION PARA GENERAR LA FLECHA DE UN PUNTO EN EL PLANO

plt.title("COVID-19 EN COLOMBIA 2021\n",
          size=50, color='#010103')

ax.plot(X, Y,
        color='yellow',
        marker='o',
        linewidth=4,
        markersize=15,
        markeredgecolor='red')