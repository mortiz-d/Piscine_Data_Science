import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

def chart_1(df):
    ax = df.plot.bar(x='intervalo', y='frecuencia', color='skyblue', figsize=(10, 6))
    ax.set_xlabel('Frecuencia')
    ax.set_ylabel('Clientes') 
    plt.show()
    return

def chart_2(df2):
    orden_precio = ['0', '50', '100', '150', '+200']
    df2['precio'] = pd.Categorical(df2['precio'], categories=orden_precio, ordered=True)
    df2 = df2.sort_values(by='precio')
    plt.bar(df2['precio'], df2['clientes'], color='skyblue')
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

    query = """
            SELECT
                intervalo,
                COUNT(user_id) AS frecuencia
            FROM (
                SELECT
                    user_id,
                    FLOOR(COUNT(*) / 10) * 10 AS intervalo
                FROM
                    customers
                WHERE
                    event_type = 'purchase'
                GROUP BY
                    user_id
            ) AS subquery
            GROUP BY
                intervalo
            HAVING
                COUNT(user_id) >= 1000
            ORDER BY intervalo ASC;
        """
    customer_data = read_customer_table(query)
    if customer_data:
        df = pd.DataFrame(customer_data, columns=['intervalo','frecuencia'])
        chart_1(df)
    
    query = """ SELECT
                    CASE 
                        WHEN gastado < 25 THEN '0'
                        WHEN gastado BETWEEN 25 AND 75 THEN '50'
                        WHEN gastado BETWEEN 75 AND 125 THEN '100'
                        WHEN gastado BETWEEN 125 AND 175 THEN '150'
                        ELSE '+200'
                    END AS precio,
                    COUNT(*) AS clientes
                FROM (
                    SELECT
                        user_id,
                        SUM(price) AS gastado
                    FROM
                        customers
                    WHERE
                        event_type = 'purchase'
                    GROUP BY
                        user_id
                ) AS subquery
                WHERE gastado <= 225
                GROUP BY
                    precio
                ORDER BY
                    precio;"""
    customer_data = read_customer_table(query)
    if customer_data:
        df2 = pd.DataFrame(customer_data, columns=['precio','clientes'])
        chart_2(df2)

except psycopg2.OperationalError as e:
    print(f"Error de conexión: {e}")

finally:
    print("Todo cerrado")
    cur.close()
    conn.close()
