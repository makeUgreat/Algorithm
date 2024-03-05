-- 코드를 입력하세요
select
    ins.animal_id,
    ins.animal_type,
    ins.name
from
    animal_ins ins
    inner join
    animal_outs outs
    on ins.animal_id = outs.animal_id
where
    ins.sex_upon_intake LIKE 'Intact%'
    AND (outs.sex_upon_outcome LIKE 'Spayed%'
        OR outs.sex_upon_outcome LIKE 'Neutered%')
order by ins.animal_id;
        