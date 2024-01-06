SELECT
    COUNT(user_id) AS users
FROM
    user_info
WHERE
    joined >= '2021-01-01' AND joined < '2022-01-01'
    AND age BETWEEN 20 AND 29