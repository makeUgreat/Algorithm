-- 코드를 입력하세요
SELECT
    order_id,
    product_id,
    to_char(out_date,'YYYY-mm-dd') as out_date,
    case
        when out_date is NULL then '출고미정'
        when out_date <= date '2022-05-01' then '출고완료'
        else '출고대기'
    end as 출고여부
        
from food_order
order by order_id