import pandas as pd

from Carga_datos import df_datos_pokemons
from Estadistica_Descriptiva import (calcular_promedio, calcular_mediana, calcular_moda, calcular_rango,
                                    calcular_desviacion_estandar, calcular_valor_maximo, calcular_valor_minimo)

# Muestra de Resultados

# 3.- Estadistica Descriptiva
print("\nEstadística Descriptiva de los Pokémon:\n")
promedio_ataque = calcular_promedio(df_datos_pokemons["Ataque"])
mediana_ataque = calcular_mediana(df_datos_pokemons["Ataque"])
moda_ataque = calcular_moda(df_datos_pokemons["Ataque"])

print("Ataque:")
print(f"  Promedio: {promedio_ataque}")
print(f"  Mediana: {mediana_ataque}")
print(f"  Moda: {moda_ataque}\n")

mayor_defensa = calcular_valor_maximo(df_datos_pokemons["Defensa"], df_datos_pokemons)
menor_velocidad = calcular_valor_minimo(df_datos_pokemons["Velocidad"], df_datos_pokemons)

print("Pokemon con mayor Defensa:")
print(mayor_defensa.to_string(index=False), "\n")

print("Pokemon con menor Velocidad:")
print(menor_velocidad.to_string(index=False), "\n")

rango_ps = calcular_rango(df_datos_pokemons["PS"])
desviacion_estandar_ps = calcular_desviacion_estandar(df_datos_pokemons["PS"])

print("PS (Puntos de Salud):")
print(f"  Rango: {rango_ps}")
print(f"  Desviación Estándar: {desviacion_estandar_ps}\n")

#cuantos pokemon tienen dos tipos
cantidad_pokemon_dos_tipos = len(df_datos_pokemons[df_datos_pokemons["Tipo 2"] != "Ninguno"])

print(f"Cantidad de Pokémon con dos tipos: {cantidad_pokemon_dos_tipos}\n")