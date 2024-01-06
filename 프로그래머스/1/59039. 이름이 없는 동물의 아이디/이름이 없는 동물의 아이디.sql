SELECT
    animal_id
FROM
    (
    SELECT *
    FROM animal_ins
    WHERE name is NULL
    )
ORDER BY
    animal_id