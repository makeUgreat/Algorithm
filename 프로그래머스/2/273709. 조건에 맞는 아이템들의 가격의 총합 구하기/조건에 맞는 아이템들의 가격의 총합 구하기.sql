select
    SUM(PRICE) AS TOTAL_PRICE
from
    item_info
group by
    rarity
having
    rarity = 'LEGEND'