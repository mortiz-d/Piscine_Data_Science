import psycopg2
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

def chart_1(df):
    num_clusters = 4
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(features)
    cluster_labels = kmeans.labels_
    df['cluster'] = cluster_labels
    k_range = range(1, 5)

    sse = []
    for k in k_range:
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(features)
        sse.append(kmeans.inertia_)

    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='dinero_gastado', y='dias_desde_ultima_compra', hue='cluster', data=df, palette='Set1')
    plt.title('Gráfico de dispersión de clientes agrupados por clustering')
    plt.ylabel('Dias pasados desde la última compra')
    plt.xlabel('Dinero gastado')
    plt.legend(title='Grupo')

     # Marcar los centroides correspondientes a los clusters definidos
    centroids = kmeans.cluster_centers_
    centroids = kmeans.cluster_centers_
    for i, centroid in enumerate(centroids):
        print("Vuelta :",i)
        plt.scatter(centroid[0], centroid[1], marker='o', s=100, c='yellow', label='Centroide')
    
    plt.show()

    return

def chart_2(df):
    num_clusters = 3
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(features)
    cluster_labels = kmeans.labels_
    cluster_names = {0: 'Cliente Nuevo', 1: 'Leal', 2: 'Inactivo'}
    df['cluster'] = cluster_labels
    df['cluster'] = df['cluster'].map(cluster_names)
    k_range = range(1, 4)
    sse = []
    for k in k_range:
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(features)
        sse.append(kmeans.inertia_)
    # order = ['Cliente Nuevo', 'Leal', 'Inactivo']
   
    plt.figure(figsize=(8, 6))
    sns.countplot(x='cluster', data=df, palette='Set1', legend=False)
    plt.title('Agrupación de clientes por categoría')
    plt.xlabel('Categoría')
    plt.ylabel('Cantidad de clientes')
    plt.xticks(rotation=45)
    plt.show()
     #Comprobar que las etiquetas son buenas
    # sns.scatterplot(x='dinero_gastado', y='dias_desde_ultima_compra', hue='cluster', data=df, legend=False, palette='Set1')
    # plt.figure(figsize=(8, 6))
    # plt.show()
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
        df = pd.DataFrame(customer_data, columns=['user_id','ultima_compra', 'dinero_gastado'])
        df['ultima_compra'] = pd.to_datetime(df['ultima_compra'])
        fecha_referencia = df['ultima_compra'].min()
        df['dias_desde_ultima_compra'] = (df['ultima_compra'] - fecha_referencia).dt.days
        features = df[['dinero_gastado', 'dias_desde_ultima_compra']]

        # chart_1(df)
        chart_2(df)

    

    
    
   


except psycopg2.OperationalError as e:
    print(f"Error de conexión: {e}")

finally:
    # Cerrar el cursor y la conexión
    print("Todo cerrado")
    cur.close()
    conn.close()


# 