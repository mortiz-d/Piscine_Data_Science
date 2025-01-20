import os
import psycopg2
from psycopg2 import sql
import pandas as pd

# Para asegurar las variables de entorno
def read_env(filename='../ex00/.env'):
    env_vars = {}
    with open(filename, 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.strip().split('=', 1)
                env_vars[key] = value
    return env_vars

#Comprobaciones de si existen para no crearlas de nuevo
def enum_exists():
    check_enum_sql = """
    SELECT EXISTS (
        SELECT 1
        FROM pg_type
        WHERE typname = 'event_enum'
        AND typtype = 'e'
    );
    """
    try:
        cur.execute(check_enum_sql)
        exists = cur.fetchone()[0]
        return exists
    except psycopg2.Error as e:
        conn.rollback()
        return False

def table_exists(table_name):
    query = """
    SELECT EXISTS (
        SELECT 1
        FROM information_schema.tables
        WHERE table_name = %s
    );
    """


    try:
        cur.execute(query, (table_name,))
        exists = cur.fetchone()[0]
        return exists
    except psycopg2.Error as e:
        conn.rollback()
        return False

#Creamos el enum
def create_enum ():
    event_enum_sql = """
    CREATE TYPE event_enum AS ENUM (
        'purchase',
        'view',
        'cart',
        'remove_from_cart'
    );
    """
    if not enum_exists() : 
        try:
            cur.execute(event_enum_sql)
            conn.commit()
            print("se creo el evento enum exitosamente")
        except psycopg2.Error as e:
            print("No se pudo crear el evento enum:", e)
            conn.rollback()
    else :
        print ("TYPE event_enum ya existe por lo que no se crea")
    return

#Creamos la tabla
def create_table (table_name):
    #La puta tabla si que la he complicado
    create_table_sql = psycopg2.sql.SQL("""
    CREATE TABLE {} (
        event_time TIMESTAMP,
        event_type event_enum,
        product_id INTEGER,
        price NUMERIC(10, 2),
        user_id BIGINT,
        user_session UUID
    );
    """).format(psycopg2.sql.Identifier(table_name))

    if not table_exists(table_name):
        try:
            cur.execute(create_table_sql)
            conn.commit()
            print("Tabla ",table_name," creada exitosamente.")
        except psycopg2.Error as e:
            print("No se pudo crear la tabla ",table_name,":", e)
            conn.rollback()
    else :
        print ("La tabla ", table_name, " ya existe no se crea de nuevo")

    return

#Aqui empieza lo bueno
directory = './zips/customer/'
env_vars = read_env()

try :
    #Nos conectamos a la BBDD
    conn = psycopg2.connect(
        dbname      = env_vars.get('POSTGRES_DB'),
        user        = env_vars.get('POSTGRES_USER'),
        password    = env_vars.get('POSTGRES_PASSWORD'),
        host        = env_vars.get('SERVER_NAME_POSTGRESS'),
        port        = env_vars.get('EXTERNAL_PORT_POSTGRES')
    )
    print("Conexión exitosa a la base de datos PostgreSQL.")
    
    # Creamos el cursor para realizar transacciones (metodo seguro para CRUD)
    cur = conn.cursor()
    create_enum()
    create_table("data_2022_dec")
    create_table("data_2022_nov")
    create_table("data_2022_oct")
    create_table("data_2023_jan")
    

except psycopg2.OperationalError as e:
    print(f"Error de conexión: {e}")

finally:
    # Cerrar el cursor y la conexión
    print("Todo cerrado")
    cur.close()
    conn.close()
