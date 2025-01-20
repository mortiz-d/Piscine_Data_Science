import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def gen_img_train(df_train,img_name, x_column, y_column, separador):
    
    plt.figure(figsize=(8, 6))
    sith_data = df_train[df_train[separador] == 'Sith']
    jedi_data = df_train[df_train[separador] == 'Jedi']

    plt.scatter(sith_data[x_column], sith_data[y_column], color='red', alpha=0.5, label='Sith')
    plt.scatter(jedi_data[x_column], jedi_data[y_column], color='blue', alpha=0.5, label='Jedi')


    plt.title(f'Relación entre {x_column} y {y_column}')
    plt.xlabel(f'{x_column}')
    plt.ylabel(f'{y_column}')
    plt.grid(True)
    plt.savefig(f'{img_name}.png')
    return

df_test = pd.read_csv("../Test_knight.csv",index_col=False)
df_train = pd.read_csv("../Train_knight.csv",index_col=False)

# Hacemos bullyng a la columna por ser texto
categorical_columns = ['knight']
numeric_columns = [col for col in df_train.columns if col not in categorical_columns]

scaler = MinMaxScaler()
df_train[numeric_columns] = scaler.fit_transform(df_train[numeric_columns])
df_test[numeric_columns] = scaler.fit_transform(df_test[numeric_columns])
# Mostrams el df ahora siendo normal
print("DataFrame de prueba normalizado:")
print(df_test.head())

print("\nDataFrame de entrenamiento normalizado:")
print(df_train.head())

gen_img_train(df_train,"Mezclados_train","Reactivity", "Agility", "knight")