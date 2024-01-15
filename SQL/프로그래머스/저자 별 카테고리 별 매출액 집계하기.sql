SELECT
    a.author_id AS AUTHOR_ID,
    a.author_name AS AUTHOR_NAME,
    b.category AS CATEGORY, 
    sum(b.price *s.sales) AS TOTAL_SALES
FROM book b
JOIN book_sales s
ON b.book_id = s.book_id
JOIN author a
ON b.author_id = a.author_id
WHERE date_format(s.sales_date, '%Y%m') = 202201
GROUP BY a.author_id, b.category
ORDER BY a.author_id asc, b.category desc