import os
import time

# Registra el tiempo actual antes de ejecutar la consulta


# Aquí va tu código para ejecutar la consulta
# ...

# Registra el tiempo actual después de ejecutar la consulta


# Calcula la diferencia de tiempo


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
move_clean = f"docker cp remove_duplicates.sql postgres-container:var/lib/postgresql/data/remove_duplicates.sql"
os.system(move_clean)
inicio = time.time()
clean_dups = f"docker exec -i postgres-container psql -U {user} -d {dbname} --single-transaction -f  /var/lib/postgresql/data/remove_duplicates.sql"
print("Eliminando duplicados -> ",clean_dups)
os.system(clean_dups)
fin = time.time()
duracion = fin - inicio
print("La consulta tomó", duracion, "segundos en ejecutarse.")
print("Duplicados eliminados")
erase_sql = f"docker exec -i postgres-container rm /var/lib/postgresql/data/remove_duplicates.sql"
os.system(erase_sql)
print("Eliminando script del docker")