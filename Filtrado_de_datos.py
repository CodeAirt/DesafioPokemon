import pandas as pd
from Carga_datos import df_datos_pokemons

# Filtrado de datos

#filtrar pokemons tipo fuego
df_pokemon_tipo_fuego = df_datos_pokemons[df_datos_pokemons["Tipo 1"] == "Fuego"][["Nombre","Tipo 1","Ataque","Velocidad"]]

print("\nPokemons de tipo Fuego:")
print(df_pokemon_tipo_fuego.to_string(index=False))
