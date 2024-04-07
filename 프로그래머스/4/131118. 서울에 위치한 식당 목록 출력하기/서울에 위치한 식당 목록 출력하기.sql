select
    i.rest_id,
    i.rest_name,
    i.food_type,
    i.favorites,
    i.address,
    round(avg(r.review_score),2) as score
    
from
    rest_info i
    inner join rest_review r on r.rest_id = i.rest_id
where
    i.address like '서울%'
group by
    i.rest_id
order by
    score desc, i.favorites desc;
    