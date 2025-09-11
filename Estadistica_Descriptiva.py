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

#funcion calcular rango
def calcular_rango(columna):
    return (columna.max() - columna.min()).round(1)

#funcion calcular desviacion estandar
def calcular_desviacion_estandar(columna):
    return np.std(columna).round(1) #agregar dentro de std() ddof=1 para muestra, numpy por defecto es poblacion(ddof=0)

#funcion calcular mayor valor
def calcular_valor_maximo(columna, df_datos_pokemons): #recibe nombre de la columna y el dataframe
    return df_datos_pokemons.loc[[columna.idxmax()], ["Nombre", columna.name]]  #devuelve la fila del dataframe donde se encuentra el valor max y en corchetes se especifica que datos mostrar del dataframe

#funcion calcular menor valor
def calcular_valor_minimo(columna, df_datos_pokemons):
    return df_datos_pokemons.loc[[columna.idxmin()], ["Nombre", columna.name]] #.loc para manipular datos del dataframe utilizando etiquetas (nombres de filas y columnas)
