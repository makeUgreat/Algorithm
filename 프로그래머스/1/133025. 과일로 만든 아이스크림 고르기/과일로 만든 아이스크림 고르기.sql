select fh.flavor
from first_half fh inner join icecream_info ic
on fh.flavor = ic.flavor
where total_order >= 3000
and ingredient_type = 'fruit_based'
order by total_order desc;