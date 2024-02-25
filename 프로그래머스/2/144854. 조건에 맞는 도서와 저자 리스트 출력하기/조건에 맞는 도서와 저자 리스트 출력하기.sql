select book_id, author_name, to_char(published_date, 'yyyy-mm-dd') as published_date
from book a inner join author b
on a.author_id = b.author_id
where category = '경제'
order by published_date