SELECT j.flavor
FROM (
    SELECT flavor, sum(total_order) AS total_order
    FROM july
    GROUP BY flavor
) AS j
JOIN first_half AS h
ON j.flavor = h.flavor
GROUP BY j.flavor
ORDER BY j.total_order + h.total_order DESC
LIMIT 3