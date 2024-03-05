select
    book_id,
    to_char(published_date,'yyyy-mm-dd') published_date
from
    book
where 
    to_char(published_date,'yyyy') like '2021%'
    and category = '인문'
order by
    published_date;