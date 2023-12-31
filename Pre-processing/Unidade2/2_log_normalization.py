import numpy as np
from src.utils import load_wine_dataset
import pandas as pd

wine = load_wine_dataset()

pd.set_option('display.max_columns', None)

#print as caractéristicas estatísticas do dataset wine
print(wine.describe)

## Aplique a função de nomarlização logarítmica na coluna Proline
wine["log_2"] = np.log(wine["Proline"])

# Print a variância da coluna proline
print(wine[["Proline", "log_2"]].var())

# print a variância da coluna proline normalizada
print(np.var(wine['log_2']))