import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from Carga_datos import df_datos_pokemons
from visualizacion_de_datos import grafico_dispersion, boxplot

# Analisis exploratorio de datos (EDA)
print("\nAnalisis Exploratorio de Datos (EDA):")

#punto 1.-
print("\n1.-Que tipos de pokemon tienen mayor Ataque o Defensa?")

#calculo promedio de ataque y defensa por tipo
promedio_ataque_por_tipo = df_datos_pokemons.groupby("Tipo 1")["Ataque"].mean().reset_index().sort_values(by="Ataque", ascending=False)

print("\nPromedio de Ataque por Tipo de Pokemon (mayor a menor):")
print(promedio_ataque_por_tipo.round(1).to_string(index=False))

promedio_defensa_por_tipo = df_datos_pokemons.groupby("Tipo 1")["Defensa"].mean().reset_index().sort_values(by="Defensa", ascending=False)

print("\nPromedio de Defensa por Tipo de Pokemon (mayor a menor):")
print(promedio_defensa_por_tipo.round(1).to_string(index=False))

print("\nJustificacion: Los tipo Lucha y Dragon tienden a tener el mayor ataque promedio, " \
    "mientras que los tipo Roca y Tierra tienen mayor defensa.")

#punto 2.-
print("\n2.-Hay correlacion entre Ataque y Velocidad?")

correlacion = df_datos_pokemons[['Ataque', 'Velocidad']].corr()
coeficiente = correlacion.loc['Ataque', 'Velocidad']

print(f"\nEl coeficiente de correlacion entre Ataque y Velocidad es: {coeficiente:.2f}")

if coeficiente > 0.4:
    print("Existe una correlacion positiva moderada. Los Pokemon con mas ataque tienden a tener mas velocidad.")
elif coeficiente < -0.4:
    print("Existe una correlacion negativa moderada.")
else:
    print("La correlacion lineal es debil.")

#punto 3.-
print("\n3.-Que tan dispersos estan los PS por cada tipo?")

desviacion_ps_por_tipo = df_datos_pokemons.groupby('Tipo 1')['PS'].std().sort_values(ascending=False)

print("\nDesviacion Estandar de PS por tipo (dispersion de mayor a menor):")
print(desviacion_ps_por_tipo.round(1))
print("\nEl tipo Normal es el que presenta mayor dispersion en PS, " \
    "esto se debe a que incluye Pokemons con PS muy bajos y otros con PS extremadamente altos como Chansey.")

#punto 4.-
print("\n4.-Identificando outliers en los valores de Ataque y PS con Boxplots")

boxplot(df_datos_pokemons["Tipo 1"], df_datos_pokemons["Ataque"], "Tipo 1", "Ataque") #funcion boxplot para ver la distribucion de Ataque en cada tipo

boxplot(df_datos_pokemons["Tipo 1"], df_datos_pokemons["PS"], "Tipo 1", "PS") #funcion boxplot para ver la distribucion de PS en cada tipo

print("\nEn los graficos generados cualquier punto que aparezca por encima o por debajo de las lineas del diagrama de caja" \
    " es un posible outlier. Por ejemplo, en los PS del tipo Normal, Chansey aparece como outlier por su alto valor.\n")