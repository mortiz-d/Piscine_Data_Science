# -*- coding: utf-8 -*-
import os

# Para asegurar las variables de entorno
def read_env(filename='../ex00/.env'):
    env_vars = {}
    with open(filename, 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.strip().split('=', 1)
                env_vars[key] = value
    return env_vars


#Aqui empieza lo bueno

env_vars = read_env()

dbname      = env_vars.get('POSTGRES_DB'),
user        = env_vars.get('POSTGRES_USER'),
host        = env_vars.get('SERVER_NAME_POSTGRESS'),
port        = env_vars.get('EXTERNAL_PORT_POSTGRES')
directory = './zips/item/'
table_name = "customers_table"
try :
    print("Creamos la tabla -> ",table_name)
    ruta_destino_contenedor = f"/var/lib/postgresql/data/{table_name}"
            
    # Copiar el archivo SQL al contenedor PostgreSQL
    comando_copiar = f"docker cp {table_name}.sql postgres-container:{ruta_destino_contenedor}.sql"
    print("Moviendo SQL a Docker")
    os.system(comando_copiar)
    # Ejecutar el archivo SQL dentro del contenedor PostgreSQL
    aplicacion = f"docker exec -i postgres-container psql -U {user[0]} -d {dbname[0]} -f {ruta_destino_contenedor}.sql"
    print(aplicacion)
    os.system(aplicacion)
    print("Hemos terminado con la tabla ->",table_name)
except Exception as e:
    print("Ocurrió un error:", str(e))
finally:
    # Cerrar el cursor y la conexión
    print("Todo cerrado")






