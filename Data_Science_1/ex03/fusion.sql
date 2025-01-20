-- SELECT 
--     c.event_time,
--     c.event_type,
--     c.product_id,
--     c.price,
--     c.user_id,
--     c.user_session,
--     i.category_id,
--     i.category_code,
--     i.brand
-- FROM 
--     customer_5feb2023 AS c
-- JOIN 
--     item AS i ON c.product_id = i.product_id;

CREATE TABLE IF NOT EXISTS customers (
    event_time TIMESTAMP,
    event_type event_enum,
    product_id INTEGER,
    price NUMERIC(10, 2),
    user_id BIGINT,
    user_session UUID,
    category_id NUMERIC,
    category_code TEXT,
    brand TEXT
);

INSERT INTO customers (event_time, event_type, product_id, price, user_id, user_session, category_id, category_code, brand)
SELECT 
    c.event_time,
    c.event_type,
    c.product_id,
    c.price,
    c.user_id,
    c.user_session,
    i.category_id,
    i.category_code,
    i.brand
FROM 
    customer_free_dup c
LEFT JOIN 
    (
        SELECT 
            product_id,
            COALESCE(MIN(i.category_id), NULL) AS category_id,
            COALESCE(MIN(i.category_code), NULL) AS category_code,
            COALESCE(MIN(i.brand), NULL) AS brand
        FROM  
            item AS i
        GROUP BY 
            product_id
    ) i ON c.product_id = i.product_id;

DROP TABLE customer_free_dup;
DROP TABLE customer_dup;