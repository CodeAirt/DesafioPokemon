import pandas as pd
import numpy as np

from Carga_datos import df_datos_pokemons

#funcion calculo promedio
def calcular_promedio(columna):
    return np.mean(columna).round(1)

#funcion calculo mediana
def calcular_mediana(columna):
    return np.median(columna).round(1)

#funcion calculo moda
def calcular_moda(columna):
    return columna.mode()[0] if not columna.mode().empty else None # Si hay multiples modas, devuelve la primera con [0]. El if es para manejar el caso de moda vacia.(devuelve None)

