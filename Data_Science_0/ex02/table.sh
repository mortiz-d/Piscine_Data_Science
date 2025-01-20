#!/bin/bash

# Nombre del archivo CSV
csv_file="datos.csv"

# Nombre de la tabla SQL
table_name="mi_tabla"

enum="CREATE TYPE event_enum AS ENUM (
    'purchase',
    'view',
    'cart',
    'remove_from_cart'
);"

crear="CREATE TABLE data_2022_dec (
    event_time TIMESTAMP,
    event_type event_enum,
    product_id INTEGER,
    price NUMERIC(10, 2),
    user_id INTEGER,
    user_session VARCHAR(100)
);"


echo "Script SQL generado: salida.sql"
