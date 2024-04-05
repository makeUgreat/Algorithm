select 
    car_id,
    max(CASE
        when to_date('2022-10-16','yyyy-mm-dd') between start_date and end_date then '대여중'
        else '대여 가능'
    end) as availability
from car_rental_company_rental_history
group by car_id
order by car_id desc

-- select
--     car_id,
--     CASE
--         when to_date('2022-10-16','yyyy-mm-dd') between start_date and end_date then '대여중'
--         else '대여가능'
--     end as availability
-- from (
--     select *
--     from car_rental_company_rental_history
--     where to_date('2022-10-16','yyyy-mm-dd') between start_date and end_date
-- )