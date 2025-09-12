import pandas as pd
import numpy as np

from Carga_datos import df_datos_pokemons
from Estadistica_Descriptiva import (calcular_promedio, calcular_mediana, calcular_desviacion_estandar,
                                     calcular_valor_maximo, calcular_valor_minimo)
from Filtrado_de_datos import filtrar_pokemons_por_tipo

#estadisticas de ataque por cada tipo de pokemon
tipos_unicos = df_datos_pokemons["Tipo 1"].unique() #deja uno de cada tipo
promedios_de_velocidad = {} #diccionario promedios velocidad por tipo

for tipo in tipos_unicos: #recorre cada tipo
    df_tipo = filtrar_pokemons_por_tipo(tipo) #llama funcion que devuelve un dataframe con los pokemon de un tipo
    if not df_tipo.empty:
        promedio_ataque = calcular_promedio(df_tipo["Ataque"])
        mediana_ataque = calcular_mediana(df_tipo["Ataque"])
        desviacion_estandar_ataque = calcular_desviacion_estandar(df_tipo["Ataque"])

        print(f"\nEstadisticas de Ataque para Pokemons de tipo {tipo}:")
        print(f"  Promedio: {promedio_ataque}")
        print(f"  Mediana: {mediana_ataque}")
        print(f"  Desviacion Estandar: {desviacion_estandar_ataque}")

        #velocidaad
        promedio_velocidad = calcular_promedio(df_tipo["Velocidad"])
        promedios_de_velocidad[tipo] = promedio_velocidad #guarda los promedios de velocidad por tipo (formato diccionario)

        #PS
        mayor_ps = calcular_valor_maximo(df_tipo["PS"], df_tipo)
        menor_ps = calcular_valor_minimo(df_tipo["PS"], df_tipo)

        print(f"\n  Pokemon con MAYOR PS de tipo {tipo}:")
        print(mayor_ps.to_string(index=False), "\n")
        print(f"  Pokemon con MENOR PS de tipo {tipo}:")
        print(menor_ps.to_string(index=False), "\n")

if promedios_de_velocidad: #si el diccionario no esta vacio, si lo esta no hace nada
    tipo_mas_rapido = max(promedios_de_velocidad, key=promedios_de_velocidad.get) #key es para el maximo segun el valor del diccionario
    print(f"\nEl tipo de pokemon con mayor promedio de Velocidad es:")
    print(f"  Tipo {tipo_mas_rapido} con un promedio de {promedios_de_velocidad[tipo_mas_rapido]}\n")
