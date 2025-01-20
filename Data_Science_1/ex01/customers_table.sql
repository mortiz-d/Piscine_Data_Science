DO $$
DECLARE
    v_table_name TEXT;
    sql_query TEXT := '';
    dynamic_query TEXT;
BEGIN
    --Creamos el cliente definitivo
    CREATE TABLE IF NOT EXISTS customer_dup (
        event_time TIMESTAMP,
        event_type event_enum,
        product_id INTEGER,
        price NUMERIC(10, 2),
        user_id BIGINT,
        user_session UUID
    );
    -- Construye la consulta dinámica para unir las tablas
    FOR v_table_name IN 
        SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE 'data_202%'
    LOOP
        sql_query := sql_query || 'SELECT * FROM ' || quote_ident(v_table_name) || ' UNION ALL ';
    END LOOP;

    -- Elimina el último ' UNION ALL '
    sql_query := LEFT(sql_query, LENGTH(sql_query) - 10);

    -- Construye la consulta dinámica completa
    dynamic_query := 'INSERT INTO customer_dup ' || sql_query;

    -- Ejecuta la consulta dinámica
    EXECUTE dynamic_query;
END $$;