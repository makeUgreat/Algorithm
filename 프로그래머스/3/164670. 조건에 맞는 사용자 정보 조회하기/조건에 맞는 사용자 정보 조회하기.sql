-- 코드를 입력하세요
SELECT
    user_id,
    nickname,
    city || ' ' || street_address1 || ' ' || street_address2 as 전체주소,
    substr(B.TLNO, 1,3) || '-' || substr(B.TLNO, 4,4) || '-' || substr(B.TLNO, 8,4) 전화번호
from
    used_goods_user b
where
    b.user_id in (
    select writer_id
    from used_goods_board
    group by writer_id
    having count(1) >= 3)
order by
    user_id desc