select
    a.food_type,
    rest_id,
    rest_name,
    a.favorites
from rest_info a inner join (
    select
        food_type,
        max(favorites) as mx_fav
    from rest_info
    group by food_type 
) b on a.food_type = b.food_type and a.favorites = b.mx_fav
order by
    food_type desc;