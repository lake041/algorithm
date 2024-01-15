SELECT car_id, car_type, fee
FROM (
    SELECT c.car_id, c.car_type, c.daily_fee * 30 * (100 - p.discount_rate) / 100 AS fee
    FROM car_rental_company_car c
    JOIN car_rental_company_discount_plan p
    ON c.car_type = p.car_type AND p.duration_type = '30일 이상'
    WHERE c.car_type IN ('세단', 'SUV')
    AND c.car_id NOT IN (
        SELECT DISTINCT car_id
        FROM car_rental_company_rental_history
        WHERE start_date <= TO_DATE('2022-11-30', 'YYYY-MM-DD')
        AND TO_DATE('2022-11-01', 'YYYY-MM-DD') <= end_date
    )
)
WHERE 500000 <= fee AND fee < 2000000
ORDER BY fee DESC, car_type ASC, car_id DESC