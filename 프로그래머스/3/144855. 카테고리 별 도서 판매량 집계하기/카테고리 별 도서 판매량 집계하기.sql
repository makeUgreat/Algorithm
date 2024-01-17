SELECT
    A.category,
    SUM(B.sales) AS totl_sales
FROM book A INNER JOIN book_sales B
ON A.book_id = B.book_id
WHERE
    TO_CHAR(B.sales_date,'YYYY-MM') = '2022-01'
GROUP BY A.category
ORDER BY A.category