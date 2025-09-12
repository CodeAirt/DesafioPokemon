import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from Carga_datos import df_datos_pokemons

#Visualizacion de Datos

#histograma de unna columna
def histograma(columna, titulo, xlabel): #recibe la columna a graficar por medio del dataframe, el titulo del grafico y el nombre del eje x
    sns.histplot(columna, bins=10, kde=True) #kde=True para agregar la curva de densidad
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel("Frecuencia")
    plt.show()

#grafico dispersion x vs y
def grafico_dispersion(columna_x, columna_y, titulo, xlabel, ylabel): #recibe las dos columnas a graficar x y respectivamente por medio del dataframe, el titulo del grafico y nombre de los ejes x y
    sns.scatterplot(x=columna_x, y=columna_y)
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

#boxplot
def boxplot(columna_x,columna_y, xlabel, ylabel,): #recibe las dos columnas a graficar x y respectivamente por medio del dataframe, el nombre de los ejes x y
    sns.boxplot(x=columna_x, y=columna_y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(f"Boxplot de {ylabel} por {xlabel}") #se agrega al titulo las variables que se estan graficando
    plt.show()

#diagrama de violin
def diagrama_violin(columna_y, ylabel):
    sns.violinplot(y=columna_y)
    plt.ylabel(ylabel)
    plt.title(f"Diagrama de Violin de la Distribucion de {ylabel}") #se agrega al titulo la variable que se esta graficando
    plt.show()
