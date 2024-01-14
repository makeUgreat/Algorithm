SELECT
    HOUR,
    COUNT(HOUR) AS COUNT
FROM
    (
    SELECT to_number(to_char(datetime,'HH24')) as HOUR
    FROM animal_outs
    )
WHERE
    HOUR BETWEEN 09 AND 19
GROUP BY
    HOUR
ORDER BY
    HOUR
    
-- select hour, count(hour) count
-- from (SELECT to_number(to_char(datetime, 'HH24')) as hour
--         from ANIMAL_OUTS)
-- where hour>=9 and hour<20
-- group by hour
-- order by hour