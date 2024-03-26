# animal_outs에는 있는데 animal_ins 는 없는 테이블 찾기

select
    outs.animal_id,
    outs.name
from
    animal_outs outs left join animal_ins ins
    on outs.animal_id = ins.animal_id
where
    ins.animal_id is null
order by
    ins.animal_id,
    ins.name