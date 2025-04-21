import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Modules Imported")

direction_train = "../Train_knight.csv"

def plot_heatmap_correlation(frame):
    ax= plt.subplot()
    sns.heatmap(frame, annot=False, ax = ax)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', fontsize=8)
    ax.set_yticklabels(ax.get_yticklabels(), rotation=0, fontsize=8)
    ax.set_xlabel('Columns')
    ax.set_ylabel('Columns')
    ax.set_title('Correlation Matrix'); 
    plt.show()

data = pd.read_csv(direction_train)
#Transformamos el caballero de tipo categorico a numerico
data["knight"] = data["knight"].map({"Jedi": 1, "Sith": 0})
plot_heatmap_correlation(data.corr())
