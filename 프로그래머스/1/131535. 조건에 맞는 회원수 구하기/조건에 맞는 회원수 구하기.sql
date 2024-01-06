SELECT COUNT(user_id) AS users
FROM user_info
WHERE
    TO_CHAR(JOINED,'YYYY') = '2021'
    AND (age >= 20 AND age <= 29)
