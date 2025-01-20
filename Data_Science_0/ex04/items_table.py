# -*- coding: utf-8 -*-
import os
import psycopg2
from psycopg2 import sql

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
        product_id INTEGER NOT NULL,
        category_id NUMERIC,
        category_code TEXT,
        brand TEXT
    );
TRUNCATE {};
""".format(table_name,table_name)

    return table_structure


def generate_order_csv(table_name , ruta_csv):
    enum_structure = """COPY {}(product_id, category_id, category_code, brand) FROM '{}.csv' DELIMITER ',' CSV HEADER;""".format(table_name,ruta_csv)
    return enum_structure



#Aqui empieza lo bueno
directory = '../../subjects/item/'
env_vars = read_env()

dbname      = env_vars.get('POSTGRES_DB'),
user        = env_vars.get('POSTGRES_USER'),
password    = env_vars.get('POSTGRES_PASSWORD'),
host        = env_vars.get('SERVER_NAME_POSTGRESS'),
port        = env_vars.get('EXTERNAL_PORT_POSTGRES')

try :

    # os.makedirs(os.path.dirname("../container/data/postgres-data"), exist_ok=True)
    #Buscamos dentro del directorio
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
            remove_sql = f"./{table_name}.sql"
            os.remove(remove_sql)
            
            print("Hemos terminado con la tabla ",table_name)

            
   
except psycopg2.OperationalError as e:
    print("Error de conexión: ",e)
finally:
    # Cerrar el cursor y la conexión
    print("Todo cerrado")


