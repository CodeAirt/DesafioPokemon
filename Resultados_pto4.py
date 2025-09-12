import seaborn as sns
import matplotlib.pyplot as plt

from Carga_datos import df_datos_pokemons
from visualizacion_de_datos import histograma, grafico_dispersion, boxplot, diagrama_violin

histograma(df_datos_pokemons["Ataque"], "Distribución de Ataque de los Pokémon", "Ataque")

grafico_dispersion(df_datos_pokemons["Ataque"], df_datos_pokemons["Velocidad"], "Grafico Dispersion Ataque vs Velocidad", "Ataque", "Velocidad")

boxplot(df_datos_pokemons["Tipo 1"], df_datos_pokemons["PS"], "Tipo 1", "PS")

diagrama_violin(df_datos_pokemons["Defensa"],"Defensa")
