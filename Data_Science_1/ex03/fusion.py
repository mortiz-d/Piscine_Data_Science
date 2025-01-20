import os
import time

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

dbname      = env_vars.get('POSTGRES_DB')
user        = env_vars.get('POSTGRES_USER')

print("Moviendo .sql al Docker")
move_clean = f"docker cp fusion.sql postgres-container:var/lib/postgresql/data/fusion.sql"
os.system(move_clean)
inicio = time.time()
clean_dups = f"docker exec -i postgres-container psql -U {user} -d {dbname} --single-transaction -f  /var/lib/postgresql/data/fusion.sql"
print("Fusionando datos -> ",clean_dups)
os.system(clean_dups)
print("Datos Fusionados")
fin = time.time()
duracion = fin - inicio
print("La consulta tomó", duracion, "segundos en ejecutarse.")
erase_sql = f"docker exec -i postgres-container rm /var/lib/postgresql/data/fusion.sql"
os.system(erase_sql)
print("Eliminando script del docker")