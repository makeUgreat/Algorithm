select a.product_code, sum( a.price * b.sales_amount ) as sales
from product a
inner join offline_sale b
on a.product_id = b.product_id
group by a.product_code
order by sales desc, a.product_code