import pandas as pd

from Carga_datos import df_datos_pokemons

#columna Poder Total
df_pokemons_con_poder_total = df_datos_pokemons.copy() #crea una copia del dataframe original para no modificarlo directamente

df_pokemons_con_poder_total["Poder Total"] = df_pokemons_con_poder_total["Ataque"] + df_pokemons_con_poder_total["Defensa"] + df_pokemons_con_poder_total["Velocidad"] + df_pokemons_con_poder_total["PS"]

print("\nDatos de los Pokemon con la nueva columna 'Poder Total':")
print(df_pokemons_con_poder_total)

#dataframe ordenado por Poder Total de mayor a menor
df_pokemons_ordenados_por_poder = df_pokemons_con_poder_total.sort_values(by="Poder Total", ascending=False)

print("\nPokemon ordenados por 'Poder Total' de mayor a menor:")
print(df_pokemons_ordenados_por_poder.to_string(index=False))