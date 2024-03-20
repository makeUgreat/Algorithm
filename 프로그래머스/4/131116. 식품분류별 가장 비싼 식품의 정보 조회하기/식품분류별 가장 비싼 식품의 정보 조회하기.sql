-- 코드를 입력하세요
-- 1. 카테고리별로 가격이 제일 비싼 상품들만 조회
-- 2. 전체 상품에서 가격이 제일 비싼 상품의 가격과 이너조인
-- 3. 이너 조인하고 카테고리, 가격, 상품이름 조회

select
    fp.category,
    max_fp.max_price,
    fp.product_name
from
    (
    select
        max(price) as max_price,
        category
    from
        food_product
    group by category
    ) max_fp 
    inner join food_product fp on max_fp.category = fp.category
    and max_fp.max_price = fp.price
where
    fp.category in ('과자','국','김치','식용유')
order by
    max_fp.max_price desc;
 

    
