import pandas as pd
from Filtrado_de_datos import filtrar_pokemons_por_tipo

#filtrar pokemons tipo fuego
print("\nPokemons de tipo Fuego:")
print(filtrar_pokemons_por_tipo("Fuego")[["Nombre","Tipo 1","Ataque","Velocidad"]].to_string(index=False)) #muestra lo pokemon filtradoss, solo muestra las columnas relevantes