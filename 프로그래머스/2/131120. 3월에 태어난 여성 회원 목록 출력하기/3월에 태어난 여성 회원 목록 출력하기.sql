select
    member_id,
    member_name,
    gender,
    to_char(date_of_birth,'yyyy-mm-dd') DATE_OF_BIRTH
from
    member_profile
where
    to_char(date_of_birth,'mm') = '03'
    and
    TLNO is not null
    and
    gender = 'W'
order by
    member_id

