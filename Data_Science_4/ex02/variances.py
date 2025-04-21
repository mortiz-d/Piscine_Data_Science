import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
import numpy as np
import seaborn as sns

def plot_variance(ratio):
    plt.figure(figsize=(8, 5))
    plt.plot(np.arange(1, len(ratio)+1), ratio, marker='.', label='Varianza acumulada')
    plt.axhline(y=0.9, color='orange', linestyle='--', label='Limite del 90%')
    plt.title('Varianza Acumulativa por Skill')
    plt.xlabel('Número de Skills')
    plt.ylabel('Proporción de Varianza Acumulada')
    plt.xticks(np.arange(1, len(ratio)+1))
    plt.legend()
    plt.tight_layout()
    plt.show()

def calculate_variance(data):
	variances = data.var().sort_values(ascending=False) #calculamos la varianza y la ordenamos de forma que se muestre

	varianza_acumulativa = variances.cumsum()
	varianza_total = variances.sum()
	ratio = varianza_acumulativa / varianza_total
	plot_variance(ratio)

direction_train = "../Train_knight.csv"
data = pd.read_csv(direction_train)
data["knight"] = data["knight"].map({"Jedi": 1, "Sith": 0})

scaler = MinMaxScaler()
data_normalized = scaler.fit_transform(data)

# Convertimos de nuevo a DataFrame para que sea legible
data_normalized = pd.DataFrame(data_normalized, columns=data.columns)

#Calculamos la varianza con los datos normalizados
calculate_variance(data_normalized)
#Calculamos la varianza con los datos sin normalizar
calculate_variance(data)

