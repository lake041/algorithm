WITH [cte_name] AS (
    SELECT [column_name(s)]
    FROM [table_name]
    WHERE [condition]
)
SELECT [column_name(s)]
FROM [table_name]
JOIN [cte_name] ON [join_condition]
WHERE [condition];