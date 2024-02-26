-- 코드를 입력하세요
SELECT 
    order_id, 
    product_id, 
    date_format(out_date,'%Y-%m-%d') as out_date,
    CASE
        WHEN out_date IS NULL THEN '출고미정'
        WHEN out_date <= DATE '2022-05-01' THEN '출고완료'
        ELSE '출고대기'
    END AS 출고여부
FROM
    food_order
order by
    order_id;