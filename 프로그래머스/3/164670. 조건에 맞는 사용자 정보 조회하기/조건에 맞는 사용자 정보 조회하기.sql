
SELECT
    user.user_id,
    nickname,
    concat(city,' ',street_address1,' ',street_address2) as 전체주소,
    concat(substr(tlno,1,3),'-',substr(tlno,4,4),'-',substr(tlno,8,4)) as 전화번호
from
    used_goods_board board inner join used_goods_user user
    on board.writer_id = user.user_id
group by user_id
having count(user_id) >= 3
order by user.user_id desc