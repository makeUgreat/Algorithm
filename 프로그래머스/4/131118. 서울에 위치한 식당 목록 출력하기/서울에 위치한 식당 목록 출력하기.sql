select
    i.rest_id,
    i.rest_name,
    i.food_type,
    i.favorites,
    i.address,
    j.score
from rest_info i
    inner join (
        select
            rest_id,
            round(avg(review_score),2) as score
        from
            rest_review
        group by
            rest_id
    ) j on i.rest_id = j.rest_id

where
    i.address like '서울%'
order by
    score desc, favorites desc;