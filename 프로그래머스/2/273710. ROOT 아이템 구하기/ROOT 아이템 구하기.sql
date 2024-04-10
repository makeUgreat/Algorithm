select
    a.item_id,
    a.item_name
from
    item_info a
    inner join (
        select item_id
        from item_tree
        where parent_item_id is null) b on b.item_id = a.item_id
order by
    a.item_id