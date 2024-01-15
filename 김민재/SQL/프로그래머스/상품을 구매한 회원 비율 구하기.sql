SELECT
    year(s.sales_date) AS year,
    month(s.sales_date) AS month,
    count(DISTINCT s.user_id) AS purchased_users,
    round(count(DISTINCT s.user_id) / (
        SELECT count(DISTINCT user_id) FROM user_info WHERE year(joined) = 2021
    ), 1) AS purchased_ratio
FROM user_info AS i
JOIN online_sale AS s
ON i.user_id = s.user_id
WHERE year(i.joined) = 2021
GROUP BY year, month
ORDER BY year ASC, month ASC