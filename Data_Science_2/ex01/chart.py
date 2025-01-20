import psycopg2
import pandas as pd
import plotly.express as px

def show_chart_1(df):

    df['day'] = pd.to_datetime(df['day'])

    fig = px.line(df, x='day', y='unique_customer', title='Numero de compras a lo largo del tiempo')
    fig.update_xaxes(title='Fecha')
    fig.update_yaxes(title='Numero de compras')
    fig.show()
    return

def show_chart_2(df):
    # Plot the data as a line chart
    df["total_sales_in_millions"] = pd.to_numeric(df['total_sales_in_millions'])

    fig = px.bar(df, x='month', y='total_sales_in_millions', title='Total de ventas por mes en millones')
    fig.update_xaxes(title='Fecha')
    fig.update_yaxes(title='Millones de Altarians ($)')
    fig.show()
    return

def show_chart_3(df):

    df["average_spending_per_day_all_customers"] = pd.to_numeric(df['average_spending_per_day_all_customers'])

    fig = px.area(df, x='day', y='average_spending_per_day_all_customers', title='Media de gasto por cliente a lo largo del año')
    fig.update_xaxes(title='Fecha')
    fig.update_yaxes(title='Media de gasto por cliente')
    fig.show()

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

    # Lectura de los datos de la tabla 'customer'
    query = """SELECT DATE(event_time) AS day, COUNT(DISTINCT user_id) AS unique_customers FROM customers WHERE event_type = 'purchase' GROUP BY DATE(event_time);"""
    customer_data = read_customer_table(query)
    if customer_data:
        df = pd.DataFrame(customer_data, columns=['day', 'unique_customer'])
        show_chart_1(df)
    
    query = """SELECT 
                    TO_CHAR(DATE_TRUNC('month', event_time), 'Month') AS month,
                    SUM(price) / 1000000.0 AS total_sales_in_millions
                FROM customers 
                WHERE event_type = 'purchase' 
                GROUP BY DATE_TRUNC('month', event_time);"""
    customer_data = read_customer_table(query)
    if customer_data:
        df = pd.DataFrame(customer_data, columns=['month', 'total_sales_in_millions'])
        # print(df)
        show_chart_2(df)

    query = """SELECT 
                    day,
                    AVG(sum_spending_per_day) AS average_spending_per_day_all_customers
                FROM (
                    SELECT 
                        DATE_TRUNC('day', event_time) AS day,
                        user_id,
                        SUM(price) AS sum_spending_per_day
                    FROM 
                        customers
                    WHERE 
                        event_type = 'purchase' 
                    GROUP BY 
                        DATE_TRUNC('day', event_time), user_id
                ) AS subquery
                GROUP BY day;"""
    customer_data = read_customer_table(query)
    if customer_data:
        df = pd.DataFrame(customer_data, columns=['day', 'average_spending_per_day_all_customers'])
        show_chart_3(df)
   


except psycopg2.OperationalError as e:
    print(f"Error de conexión: {e}")

finally:
    # Cerrar el cursor y la conexión
    print("Todo cerrado")
    cur.close()
    conn.close()
