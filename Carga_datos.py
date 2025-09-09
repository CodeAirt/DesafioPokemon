import pandas as pd

df_datos_pokemons = pd.read_csv('pokemon_primera_gen.csv') # Carga el archivo CSV en un DataFrame

#Limpieza de datos
df_datos_pokemons["Tipo 2"] = df_datos_pokemons["Tipo 2"].fillna("Ninguno")

#Limpia tipo de datos numericos
df_datos_pokemons["Ataque"] = pd.to_numeric(df_datos_pokemons["Ataque"], errors='coerce').fillna(0) # Convierte a numérico, reemplazando errores con NaN y NaN con 0
df_datos_pokemons["Defensa"] = pd.to_numeric(df_datos_pokemons["Defensa"], errors='coerce').fillna(0)
df_datos_pokemons["Velocidad"] = pd.to_numeric(df_datos_pokemons["Velocidad"], errors='coerce').fillna(0)
df_datos_pokemons["PS"] = pd.to_numeric(df_datos_pokemons["PS"], errors='coerce').fillna(0)
