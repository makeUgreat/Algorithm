select
    ingredient_type,
    sum(total_order) as total_order
from 
    first_half as a inner join icecream_info as b
    on a.flavor = b.flavor
group by
    ingredient_type
order by total_order