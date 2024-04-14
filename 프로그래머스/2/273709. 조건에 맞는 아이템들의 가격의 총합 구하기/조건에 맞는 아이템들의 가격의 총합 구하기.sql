select
    SUM(PRICE) AS TOTAL_PRICE
from
    item_info
where
    rarity = 'LEGEND'
