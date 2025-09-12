import pandas as pd
from Carga_datos import df_datos_pokemons

# Filtrado de datos

#funcion filtrar pokemons por tipo
def filtrar_pokemons_por_tipo(tipo):
    df_filtrado = df_datos_pokemons[(df_datos_pokemons["Tipo 1"] == tipo)] #agrga a un nuevo dataframe los pokemon filtrados por tipo
    return df_filtrado
