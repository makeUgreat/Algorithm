select
    ins.animal_id,
    ins.animal_type,
    ins.name
from
    (select *
    from animal_ins
    where
        sex_upon_intake LIKE 'Intact%') as ins
    inner join animal_outs as outs
    on ins.animal_id = outs.animal_id
where
    outs.sex_upon_outcome LIKE 'Spayed%'
    OR outs.sex_upon_outcome LIKE 'Neutered%'
order by
    animal_id