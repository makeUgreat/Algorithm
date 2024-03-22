-- 코드를 입력하세요
-- 먼저 생산일자가 22년 5월인 식품들만 조회하는 서브쿼리 
-- 

select
    fo.product_id,
    fp.product_name,
    sum(fp.price * fo.amount) as total_sales
from
    food_product as fp inner join food_order as fo
    on fp.product_id = fo.product_id
where
    fo.produce_date like '2022-05%'
group by
    product_id
order by
    total_sales desc, fo.product_id