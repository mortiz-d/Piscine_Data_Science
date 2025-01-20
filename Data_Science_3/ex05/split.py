import pandas as pd
from sklearn.model_selection import train_test_split

df_train = pd.read_csv("../Train_knight.csv",index_col=False)

df_remaining, df_20_percent = train_test_split(df_train, test_size=0.2)
df_20_percent.to_csv('Validation_knight.csv', index=False)
df_remaining.to_csv(' Training_knight.csv', index=False)