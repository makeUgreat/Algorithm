select
    users.user_id,
    users.nickname,
    sum(boards.price) as total_sales
from
    used_goods_board as boards inner join used_goods_user as users
    on boards.writer_id = users.user_id
where
    status = 'DONE'
group by
    users.user_id
having
    total_sales >= 700000
order by
    total_sales