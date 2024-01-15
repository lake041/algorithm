(SELECT
    date_format(sales_date, "%Y-%m-%d") AS sales_date,
    product_id,
    user_id,
    sales_amount    
FROM online_sale
WHERE date_format(sales_date, "%Y%m") = '202203')
UNION
(SELECT
    date_format(sales_date, "%Y-%m-%d") AS sales_date,
    product_id,
    NULL AS user_id,
    sales_amount
FROM offline_sale
WHERE date_format(sales_date, "%Y%m") = 202203)
ORDER BY
    sales_date ASC,
    product_id ASC,
    user_id ASC