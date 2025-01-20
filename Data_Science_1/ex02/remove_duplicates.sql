CREATE TABLE customer_free_dup AS (
    SELECT  event_time,
            event_type,
            product_id,
            price,
            user_id,
            user_session
    FROM (
        SELECT  event_time,
                event_type,
                product_id,
                price,
                user_id,
                user_session,
                ROW_NUMBER() OVER (
                    PARTITION BY
                        event_type,
                        product_id,
                        user_id,
                        user_session,
                        DATE_TRUNC('minute',event_time)
                ) AS rn
        FROM customer_dup
    ) AS RankedEvents
    WHERE rn = 1
);