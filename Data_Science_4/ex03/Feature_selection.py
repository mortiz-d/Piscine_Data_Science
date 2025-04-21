from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LassoCV
from sklearn.metrics import r2_score
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# def calculateVIF(var_predictoras_df):
#     var_pred_labels = list(var_predictoras_df.columns)
#     num_var_pred = len(var_pred_labels)
    
#     lr_model = LinearRegression()
    
#     result = pd.DataFrame(index = ['VIF'], columns = var_pred_labels)
#     result = result.fillna(0)
    
#     for ite in range(num_var_pred):
#         x_features = var_pred_labels[:]
#         y_feature = var_pred_labels[ite]
#         x_features.remove(y_feature)
        
#         x = var_predictoras_df[x_features]
#         y = var_predictoras_df[y_feature]
        
#         lr_model.fit(var_predictoras_df[x_features], var_predictoras_df[y_feature])
        
#         result[y_feature] = 1/(1 - lr_model.score(var_predictoras_df[x_features], var_predictoras_df[y_feature]))
    
#     return result.T.sort_values(by="VIF", ascending=False)

def calculateVIF_lasso(var_predictoras_df):
    var_pred_labels = list(var_predictoras_df.columns)
    num_var_pred = len(var_pred_labels)
    
    result = pd.DataFrame(index = ['VIF'], columns = var_pred_labels)
    
    for ite in range(num_var_pred):
        x_features = var_pred_labels[:]
        y_feature = var_pred_labels[ite]
        x_features.remove(y_feature)

        x = var_predictoras_df[x_features]
        y = var_predictoras_df[y_feature]

        # Escalamos porque Lasso es sensible a la escala
        scaler = StandardScaler()
        x_scaled = scaler.fit_transform(x)
        y_scaled = StandardScaler().fit_transform(y.values.reshape(-1, 1)).ravel()

        # Lasso con validación cruzada para encontrar el mejor alpha
        lasso = LassoCV(cv=5, random_state=42, max_iter=10000)
        lasso.fit(x_scaled, y_scaled)

        r2 = lasso.score(x_scaled, y_scaled)
        vif_value = 1 / (1 - r2) if r2 < 1 else float('inf')
        result[y_feature] = vif_value

    return result.T.sort_values(by="VIF", ascending=False)


def calculateVIF(var_predictoras_df):
    var_pred_labels = list(var_predictoras_df.columns)
    num_var_pred = len(var_pred_labels)
    
    lr_model = LinearRegression()
    
    result = pd.DataFrame(index = ['VIF'], columns = var_pred_labels)
    result = result.fillna(0)
    print(result.T.head())
    
    for ite in range(num_var_pred):
        x_features = var_pred_labels[:]
        y_feature = var_pred_labels[ite]
        x_features.remove(y_feature)
        
        x = var_predictoras_df[x_features]
        y = var_predictoras_df[y_feature]
        
        lr_model.fit(var_predictoras_df[x_features], var_predictoras_df[y_feature])
        
        result[y_feature] = 1/(1 - lr_model.score(var_predictoras_df[x_features], var_predictoras_df[y_feature]))
    
    return result.T.sort_values(by="VIF", ascending=False)

direction_train = "../Train_knight.csv"
data = pd.read_csv(direction_train)
data["knight"] = data["knight"].map({"Jedi": 1, "Sith": 0})

X = data.drop("knight", axis=1)

scaler = StandardScaler()
X_normalized = scaler.fit_transform(X)
X_normalized = pd.DataFrame(X_normalized, columns=X.columns)

vif = calculateVIF_lasso(X)
print(vif)