import pandas as pd
import matplotlib.pyplot as plt

def gen_img(df,img_name):
    num_columns = len(df.columns)

    fig, axs = plt.subplots(6, 5, figsize=(15, 15))

    axs = axs.flatten()
    for i, column in enumerate(df.columns):
        if i < len(axs):
            axs[i].hist(df[column], bins=20, color='skyblue', edgecolor='black')
            axs[i].set_title(column)
            axs[i].set_ylabel('Frecuencia')

    plt.tight_layout()
    plt.savefig(f'{img_name}.png')
    return

def compare(df_train, img_name):
    knight_types = df_train["knight"].unique()
    fig, axs = plt.subplots(6, 5, figsize=(15, 15))
    axs = axs.flatten()

    for i, column in enumerate(df_train.columns):
        if i < len(axs):
            for knight_type in knight_types:
                data = df_train[df_train["knight"] == knight_type][column]
                axs[i].hist(data, bins=20, alpha=0.5, label=knight_type)
            axs[i].set_title(column)
            axs[i].set_ylabel('Frequency')
            axs[i].legend()

    plt.tight_layout()
    plt.savefig(f'{img_name}.png')


df_test = pd.read_csv("../Test_knight.csv",index_col=False)
df_train = pd.read_csv("../Train_knight.csv",index_col=False)
gen_img(df_test,"test")
compare(df_train, "compare")
print(df_test)
print(df_train)





