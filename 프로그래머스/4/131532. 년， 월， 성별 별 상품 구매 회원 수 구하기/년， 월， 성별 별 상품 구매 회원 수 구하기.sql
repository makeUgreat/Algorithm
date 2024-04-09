-- 코드를 입력하세요
SELECT
    date_format(sales_date,'%Y') as year,
    month(sales_date) as month ,
    ui.gender,
    count(distinct ui.user_id) as users
from
    online_sale os
    inner join user_info ui on os.user_id = ui.user_id
where
    ui.gender is not null
group by
    year,
    month,
    gender
order by
    year,month,gender