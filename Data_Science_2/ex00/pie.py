import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

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
def execute_query():
    query = "SELECT event_type, COUNT(*) AS event_count FROM customers GROUP BY event_type;"
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

    # Lectura de los datos de la tabla 'customer'
    customer_data = execute_query()
    if customer_data:
        df_customer = pd.DataFrame(customer_data, columns=['event_type', 'event_count'])

        # Preparar datos para el gráfico de pastel
        event_types = df_customer['event_type']
        event_counts = df_customer['event_count']

        plt.pie(event_counts, labels=event_types, autopct='%1.1f%%')
        plt.title('Distribución de tipos de eventos')

        # Show the plot
        plt.show()
    else:
        print("No se pudieron leer los datos de la tabla 'customer'.")

except psycopg2.OperationalError as e:
    print(f"Error de conexión: {e}")

finally:
    # Cerrar el cursor y la conexión
    print("Todo cerrado")
    cur.close()
    conn.close()
