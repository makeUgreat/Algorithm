select
    name,
    count(*) as COUNT
from
    animal_ins
where 
    name is not null
group by
    name
having
    count(*) >= 2
order by
    name;