select
    ingredient_type,
    sum(a.total_order) as total_order
from
    first_half a inner join icecream_info b
    on a.flavor = b.flavor
group by ingredient_type
order by total_order