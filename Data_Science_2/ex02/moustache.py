import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

def char_1(df):
    # Crear el boxplot 1
    plt.figure(figsize=(10, 6))
    plt.boxplot(df['precio'], vert=False)
    plt.show()    
    return

def char_2(df):
    box = plt.boxplot(df['precio'], vert=False, patch_artist=True,showmeans=False, showfliers=False, showcaps=True)
    for patch in box['boxes']:
        patch.set_facecolor('lightblue')
    plt.show()
    return

def char_3(df):
    suma_por_cliente = df.groupby('usuario', observed=False)['precio'].sum().reset_index().rename(columns={'precio': 'gastado'})
    box = plt.boxplot(suma_por_cliente['gastado'], patch_artist=True,showfliers=False ,vert=False)
    for patch in box['boxes']:
        patch.set_facecolor('lightblue')
    plt.show()
    return

# Función para leer las variables de entorno desde el archivo .env
def read_env(filename='../../subjects/.env'):
    env_vars = {}
    with open(filename, 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.strip().split('=', 1)
                env_vars[key] = value
    return env_vars


# Función para leer todos los resultados de la tabla 'customer'
def read_customer_table(query):
    try:
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    except psycopg2.Error as e:
        conn.rollback()
        print("Error al leer los datos de la tabla 'customer':", e)
        return None

# Configuración de la conexión y otras operaciones
env_vars = read_env()

try:
    # Conexión a la base de datos PostgreSQL
    conn = psycopg2.connect(
        dbname      = env_vars.get('POSTGRES_DB'),
        user        = env_vars.get('POSTGRES_USER'),
        password    = env_vars.get('POSTGRES_PASSWORD'),
        host        = env_vars.get('SERVER_NAME_POSTGRESS'),
        port        = env_vars.get('EXTERNAL_PORT_POSTGRES')
    )
    print("Conexión exitosa a la base de datos PostgreSQL.")
    
    # Creación del cursor para realizar transacciones
    cur = conn.cursor()

    query = """ SELECT
                    user_id AS usuario,
                    price AS precio
                FROM
                    customers
                WHERE
                    event_type = 'purchase'
                ;"""
    customer_data = read_customer_table(query)
    if customer_data:
        df = pd.DataFrame(customer_data, columns=['usuario','precio'])
        df["precio"] = pd.to_numeric(df['precio'])
        mediana = df['precio'].median()
        media = df['precio'].mean()
        quantile_25 = df['precio'].quantile(0.25)
        quantile_50 = df['precio'].quantile(0.50)
        quantile_75 = df['precio'].quantile(0.75)
        min_price = df['precio'].min()
        max_price = df['precio'].max()

        print("Mediana de los precios:", mediana)
        print("Media de los precios:", media)
        print("Primer cuartil:", quantile_25)
        print("Segundo cuartil (mediana):", quantile_50)
        print("Tercer cuartil:", quantile_75)
        print("Precio mínimo:", min_price)
        print("Precio máximo:", max_price)

        char_1(df)
        char_2(df)
        char_3(df)
except psycopg2.OperationalError as e:
    print(f"Error de conexión: {e}")

finally:
    # Cerrar el cursor y la conexión
    print("Todo cerrado")
    cur.close()
    conn.close()
