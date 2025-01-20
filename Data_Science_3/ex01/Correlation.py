import pandas as pd

df_train = pd.read_csv("../Train_knight.csv", index_col=False)

df_train['knight'] = df_train['knight'].map({'Sith': 0, 'Jedi': 1})

correlation_matrix = df_train.corr()
correlation_with_target = correlation_matrix["knight"]
sorted_correlation = correlation_with_target.abs().sort_values(ascending=False)

print("La correlacion con la columna knight:")
print(sorted_correlation)