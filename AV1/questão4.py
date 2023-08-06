
#Importe as bibliotecas necessárias.
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Carregue o dataset. Se houver o dataset atualizado, carregue o atualizado.
df = pd.read_csv(r'C:\Users\Sávio\Downloads\flavors_of_cacao_ajustado.csv')

#Normalize com a melhor normalização o conjunto de dados se houver melhoria.

X = df.drop(['Rating_Categories'], axis=1)
y = df['Rating_Categories']

scaler = StandardScaler()
X_norm = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_norm, y, test_size=0.3, random_state=42)

knn = KNeighborsClassifier()

knn.fit(X_train, y_train)
accuracia_var = knn.score(X_test, y_test)

# Plote o gráfico com o a indicação do melhor k.
neighbors = np.arange(1, 15)
train_accuracies = {}
test_accuracies = {}

for neighbor in neighbors:
    knn =KNeighborsClassifier(n_neighbors=neighbor)
    knn.fit(X_train, y_train)

    train_accuracies[neighbor] = knn.score(X_train, y_train)
    test_accuracies[neighbor] = knn.score(X_test, y_test)

print("\nTreino, acuracia: ",train_accuracies)
print("\nteste, acuracia: ", test_accuracies)
plt.title("Qual o melhor k possível:")
plt.plot(neighbors, train_accuracies.values(), label="Acurácia de treino")
plt.plot(neighbors, test_accuracies.values(), label="Acurácia de teste")
plt.legend()
plt.show()

