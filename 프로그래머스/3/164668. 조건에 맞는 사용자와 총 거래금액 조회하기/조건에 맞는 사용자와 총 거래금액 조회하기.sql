select
    b.user_id,
    b.nickname,
    sum(a.price) as total_sales
from
    used_goods_board a inner join used_goods_user b
    on a.writer_id = b.user_id
where
    status = 'DONE'
group by
    b.user_id, b.nickname
having 
    sum(a.price) >= 700000
order by
    sum(a.price)