-- 월별, 성별
select
    extract(year from sales_date) as year,
    extract(month from sales_date) as month,
    ui.gender,
    count(distinct ui.user_id) as users
from
    online_sale os
    inner join user_info ui on os.user_id = ui.user_id
where
    ui.gender is not null
group by
    extract(year from sales_date),
    extract(month from sales_date),
    ui.gender
order by
    year, month, ui.gender