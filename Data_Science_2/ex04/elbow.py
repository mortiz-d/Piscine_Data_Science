import psycopg2
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def chart_1(df):
    df['ultima_compra'] = pd.to_datetime(df['ultima_compra'])
    fecha_referencia = df['ultima_compra'].min()

    df['dias_desde_ultima_compra'] = (df['ultima_compra'] - fecha_referencia).dt.days
    features = df[['dinero_gastado', 'dias_desde_ultima_compra']]

    num_clusters = 3
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(features)
    cluster_labels = kmeans.labels_
    df['cluster'] = cluster_labels
    k_range = range(1, 11)
    sse = []
    for k in k_range:
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(features)
        sse.append(kmeans.inertia_)

    # Grafica la curva de codo
    plt.figure(figsize=(10, 6))
    plt.plot(k_range, sse, marker='o')
    plt.xlabel('Número de clusters')
    plt.ylabel('Suma de distancias al cuadrado')
    plt.title('Curva de codo para determinar K óptimo')
    plt.xticks(k_range)
    plt.grid(True)
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
directory = './zips/customer/'
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
    
    query = """SELECT
                user_id,
                MAX(event_time) AS ultima_compra,
                SUM(price) AS dinero_gastado
            FROM
                customers
            WHERE
                event_type = 'purchase'
            GROUP BY
                user_id;"""
    customer_data = read_customer_table(query)
    if customer_data:
        df2 = pd.DataFrame(customer_data, columns=['user_id','ultima_compra', 'dinero_gastado'])
        chart_1(df2)

except psycopg2.OperationalError as e:
    print(f"Error de conexión: {e}")

finally:
    # Cerrar el cursor y la conexión
    print("Todo cerrado")
    cur.close()
    conn.close()