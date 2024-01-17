SELECT
    A.category,
    SUM(B.sales) AS total_sales
FROM book as A
INNER JOIN book_sales as B
ON A.book_id = B.book_id
WHERE
    DATE_FORMAT(B.sales_date,'%Y-%m') = '2022-01'
GROUP BY category
ORDER BY category

    