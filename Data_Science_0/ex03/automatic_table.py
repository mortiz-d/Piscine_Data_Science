# -*- coding: utf-8 -*-
import os
import psycopg2
from psycopg2 import sql
import sqlalchemy
import pandas as pd



#Para transformar los datos que introducimos
def parse_dataframe (df):

    df['event_time'] = pd.to_datetime(df['event_time'])
    return df
# Para asegurar las variables de entorno
def read_env(filename='../ex00/.env'):
    env_vars = {}
    with open(filename, 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.strip().split('=', 1)
                env_vars[key] = value
    return env_vars



def generate_table_sql(table_name):
    table_structure = """CREATE TABLE IF NOT EXISTS {} (
    event_time TIMESTAMP,
    event_type event_enum,
    product_id INTEGER,
    price NUMERIC(10, 2),
    user_id BIGINT,
    user_session UUID
);
TRUNCATE {};
""".format(table_name, table_name)

    return table_structure

def generate_enum():
    enum_sql = """CREATE TYPE event_enum AS ENUM (
    'purchase',
    'view',
    'cart',
    'remove_from_cart'
);
    """
    with open(f'enum.sql', 'w') as file:
        file.write(enum_sql)
    comando_copiar = f"docker cp enum.sql postgres-container:var/lib/postgresql/data/enum.sql"
    os.system(comando_copiar)
    enum = f"docker exec -i postgres-container psql -U {user[0]} -d {dbname[0]} -f /var/lib/postgresql/data/enum.sql"
    os.system(enum)
    remove_sql = f"./enum.sql"
    os.remove(remove_sql)

    return


def generate_order_csv(table_name , ruta_csv):
    enum_structure = """COPY {}(event_time, event_type, product_id, price, user_id, user_session) FROM '{}.csv' DELIMITER ',' CSV HEADER;""".format(table_name,ruta_csv)
    return enum_structure



#Aqui empieza lo bueno
directory = '../../subjects/customer/'
env_vars = read_env()

dbname      = env_vars.get('POSTGRES_DB'),
user        = env_vars.get('POSTGRES_USER'),
password    = env_vars.get('POSTGRES_PASSWORD'),
host        = env_vars.get('SERVER_NAME_POSTGRESS'),
port        = env_vars.get('EXTERNAL_PORT_POSTGRES')

try :

    # os.makedirs(os.path.dirname("../container/data/postgres-data"), exist_ok=True)
    #Buscamos dentro del directorio
    generate_enum()

    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            # Quitamos la extensión .csv para obtener el nombre de la tabla
            table_name = os.path.splitext(filename)[0]
            print("Creamos la tabla -> ",table_name)
            ruta_destino_contenedor = f"/var/lib/postgresql/data/{table_name}"

            # Generar la estructura de la tabla
            table_sql = generate_table_sql(table_name)
            order_sql = generate_order_csv(table_name, ruta_destino_contenedor)
            # Guardar la estructura en un archivo SQL temporal
            with open(f'{table_name}.sql', 'w') as file:
                file.write(table_sql)
                file.write(order_sql)
            
            # Copiar el archivo SQL al contenedor PostgreSQL
            comando_copiar = f"docker cp {table_name}.sql postgres-container:{ruta_destino_contenedor}.sql"
            os.system(comando_copiar)
            comando_copiar_csv = f"docker cp {os.path.join(directory, filename)} postgres-container:{ruta_destino_contenedor}.csv"
            print("Moviendo CSV a Docker")
            os.system(comando_copiar_csv)
            # Ejecutar el archivo SQL dentro del contenedor PostgreSQL
            aplicacion = f"docker exec -i postgres-container psql -U {user[0]} -d {dbname[0]} -f {ruta_destino_contenedor}.sql"
            print(aplicacion)
            os.system(aplicacion)
            print("Hemos terminado con la tabla ",table_name)
            remove_sql = f"./{table_name}.sql"
            os.remove(remove_sql)

            
   
except psycopg2.OperationalError as e:
    print("Error de conexión: ",e)
finally:
    # Cerrar el cursor y la conexión
    print("Todo cerrado")

