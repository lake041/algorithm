---------------------------------------------------- assumption

-- https://www.dnews.co.kr/uhtml/view.jsp?idxno=202401310752416050252
-- 276억7000만건
-- 신한은행 20% 하나은행 5%
-- 5,534,000,000
-- 15,161,643 / 86400
-- 초당 175

-- 초당 100건, 일일 8,640,000건 3억 건 => 34.7일

---------------------------------------------------- Database 용량

SELECT
    pg_database.datname AS "Database",
    pg_size_pretty(pg_database_size(pg_database.datname)) AS "Size"
FROM pg_database;

---------------------------------------------------- Table 용량

SELECT
    schemaname || '.' || tablename AS table_name,
    pg_size_pretty(pg_total_relation_size(schemaname || '.' || tablename)) AS total_size
FROM
    pg_tables
ORDER BY
    pg_total_relation_size(schemaname || '.' || tablename) DESC;

---------------------------------------------------- index 전체 조회

SELECT
    relname AS index_name,
    pg_size_pretty(pg_relation_size(oid)) AS index_size
FROM pg_class
WHERE relkind = 'i'
ORDER BY pg_relation_size(oid) DESC;

---------------------------------------------------- index 특정 테이블 조회 (파티션에는 only 키워드가 붙는다)

SELECT
    indexname AS "Index Name",
    indexdef AS "Index Definition"
FROM pg_indexes
WHERE tablename = 'transactions';

---------------------------------------------------- partition

-- 1. 기본키 제거: 파티션 키는 반드시 기본키의 일부여야 한다. 하지만 id를 기본키의 일부로 넣을 이유가 없다. 


CREATE TABLE transactions (
    id BIGINT GENERATED ALWAYS AS IDENTITY,
    transaction_time TIMESTAMP NOT NULL,
    account_id BIGINT NOT NULL,
    transaction_location BIGINT NOT NULL,
    transaction_amount NUMERIC NOT NULL
) PARTITION BY RANGE (transaction_time);

CREATE TABLE transactions_2024_01_01 PARTITION OF transactions FOR VALUES FROM ('2024-01-01') TO ('2024-01-02');
CREATE TABLE transactions_2024_01_02 PARTITION OF transactions FOR VALUES FROM ('2024-01-02') TO ('2024-01-03');
CREATE TABLE transactions_2024_01_03 PARTITION OF transactions FOR VALUES FROM ('2024-01-03') TO ('2024-01-04');
CREATE TABLE transactions_2024_01_04 PARTITION OF transactions FOR VALUES FROM ('2024-01-04') TO ('2024-01-05');
CREATE TABLE transactions_2024_01_05 PARTITION OF transactions FOR VALUES FROM ('2024-01-05') TO ('2024-01-06');
CREATE TABLE transactions_2024_01_06 PARTITION OF transactions FOR VALUES FROM ('2024-01-06') TO ('2024-01-07');
CREATE TABLE transactions_2024_01_07 PARTITION OF transactions FOR VALUES FROM ('2024-01-07') TO ('2024-01-08');
CREATE TABLE transactions_2024_01_08 PARTITION OF transactions FOR VALUES FROM ('2024-01-08') TO ('2024-01-09');
CREATE TABLE transactions_2024_01_09 PARTITION OF transactions FOR VALUES FROM ('2024-01-09') TO ('2024-01-10');
CREATE TABLE transactions_2024_01_10 PARTITION OF transactions FOR VALUES FROM ('2024-01-10') TO ('2024-01-11');
CREATE TABLE transactions_2024_01_11 PARTITION OF transactions FOR VALUES FROM ('2024-01-11') TO ('2024-01-12');
CREATE TABLE transactions_2024_01_12 PARTITION OF transactions FOR VALUES FROM ('2024-01-12') TO ('2024-01-13');
CREATE TABLE transactions_2024_01_13 PARTITION OF transactions FOR VALUES FROM ('2024-01-13') TO ('2024-01-14');
CREATE TABLE transactions_2024_01_14 PARTITION OF transactions FOR VALUES FROM ('2024-01-14') TO ('2024-01-15');
CREATE TABLE transactions_2024_01_15 PARTITION OF transactions FOR VALUES FROM ('2024-01-15') TO ('2024-01-16');
CREATE TABLE transactions_2024_01_16 PARTITION OF transactions FOR VALUES FROM ('2024-01-16') TO ('2024-01-17');
CREATE TABLE transactions_2024_01_17 PARTITION OF transactions FOR VALUES FROM ('2024-01-17') TO ('2024-01-18');
CREATE TABLE transactions_2024_01_18 PARTITION OF transactions FOR VALUES FROM ('2024-01-18') TO ('2024-01-19');
CREATE TABLE transactions_2024_01_19 PARTITION OF transactions FOR VALUES FROM ('2024-01-19') TO ('2024-01-20');
CREATE TABLE transactions_2024_01_20 PARTITION OF transactions FOR VALUES FROM ('2024-01-20') TO ('2024-01-21');
CREATE TABLE transactions_2024_01_21 PARTITION OF transactions FOR VALUES FROM ('2024-01-21') TO ('2024-01-22');
CREATE TABLE transactions_2024_01_22 PARTITION OF transactions FOR VALUES FROM ('2024-01-22') TO ('2024-01-23');
CREATE TABLE transactions_2024_01_23 PARTITION OF transactions FOR VALUES FROM ('2024-01-23') TO ('2024-01-24');
CREATE TABLE transactions_2024_01_24 PARTITION OF transactions FOR VALUES FROM ('2024-01-24') TO ('2024-01-25');
CREATE TABLE transactions_2024_01_25 PARTITION OF transactions FOR VALUES FROM ('2024-01-25') TO ('2024-01-26');
CREATE TABLE transactions_2024_01_26 PARTITION OF transactions FOR VALUES FROM ('2024-01-26') TO ('2024-01-27');
CREATE TABLE transactions_2024_01_27 PARTITION OF transactions FOR VALUES FROM ('2024-01-27') TO ('2024-01-28');
CREATE TABLE transactions_2024_01_28 PARTITION OF transactions FOR VALUES FROM ('2024-01-28') TO ('2024-01-29');
CREATE TABLE transactions_2024_01_29 PARTITION OF transactions FOR VALUES FROM ('2024-01-29') TO ('2024-01-30');
CREATE TABLE transactions_2024_01_30 PARTITION OF transactions FOR VALUES FROM ('2024-01-30') TO ('2024-01-31');
CREATE TABLE transactions_2024_01_31 PARTITION OF transactions FOR VALUES FROM ('2024-01-31') TO ('2024-02-01');
CREATE TABLE transactions_2024_02_01 PARTITION OF transactions FOR VALUES FROM ('2024-02-01') TO ('2024-02-02');
CREATE TABLE transactions_2024_02_02 PARTITION OF transactions FOR VALUES FROM ('2024-02-02') TO ('2024-02-03');
CREATE TABLE transactions_2024_02_03 PARTITION OF transactions FOR VALUES FROM ('2024-02-03') TO ('2024-02-04');
CREATE TABLE transactions_2024_02_04 PARTITION OF transactions FOR VALUES FROM ('2024-02-04') TO ('2024-02-05');
CREATE TABLE transactions_2024_02_05 PARTITION OF transactions FOR VALUES FROM ('2024-02-05') TO ('2024-02-06');
CREATE TABLE transactions_2024_02_06 PARTITION OF transactions FOR VALUES FROM ('2024-02-06') TO ('2024-02-07');
CREATE TABLE transactions_2024_02_07 PARTITION OF transactions FOR VALUES FROM ('2024-02-07') TO ('2024-02-08');
CREATE TABLE transactions_2024_02_08 PARTITION OF transactions FOR VALUES FROM ('2024-02-08') TO ('2024-02-09');
CREATE TABLE transactions_2024_02_09 PARTITION OF transactions FOR VALUES FROM ('2024-02-09') TO ('2024-02-10');
CREATE TABLE transactions_2024_02_10 PARTITION OF transactions FOR VALUES FROM ('2024-02-10') TO ('2024-02-11');
CREATE TABLE transactions_2024_02_11 PARTITION OF transactions FOR VALUES FROM ('2024-02-11') TO ('2024-02-12');
CREATE TABLE transactions_2024_02_12 PARTITION OF transactions FOR VALUES FROM ('2024-02-12') TO ('2024-02-13');
CREATE TABLE transactions_2024_02_13 PARTITION OF transactions FOR VALUES FROM ('2024-02-13') TO ('2024-02-14');
CREATE TABLE transactions_2024_02_14 PARTITION OF transactions FOR VALUES FROM ('2024-02-14') TO ('2024-02-15');
CREATE TABLE transactions_2024_02_15 PARTITION OF transactions FOR VALUES FROM ('2024-02-15') TO ('2024-02-16');
CREATE TABLE transactions_2024_02_16 PARTITION OF transactions FOR VALUES FROM ('2024-02-16') TO ('2024-02-17');
CREATE TABLE transactions_2024_02_17 PARTITION OF transactions FOR VALUES FROM ('2024-02-17') TO ('2024-02-18');
CREATE TABLE transactions_2024_02_18 PARTITION OF transactions FOR VALUES FROM ('2024-02-18') TO ('2024-02-19');
CREATE TABLE transactions_2024_02_19 PARTITION OF transactions FOR VALUES FROM ('2024-02-19') TO ('2024-02-20');
CREATE TABLE transactions_2024_02_20 PARTITION OF transactions FOR VALUES FROM ('2024-02-20') TO ('2024-02-21');
CREATE TABLE transactions_2024_02_21 PARTITION OF transactions FOR VALUES FROM ('2024-02-21') TO ('2024-02-22');
CREATE TABLE transactions_2024_02_22 PARTITION OF transactions FOR VALUES FROM ('2024-02-22') TO ('2024-02-23');
CREATE TABLE transactions_2024_02_23 PARTITION OF transactions FOR VALUES FROM ('2024-02-23') TO ('2024-02-24');
CREATE TABLE transactions_2024_02_24 PARTITION OF transactions FOR VALUES FROM ('2024-02-24') TO ('2024-02-25');
CREATE TABLE transactions_2024_02_25 PARTITION OF transactions FOR VALUES FROM ('2024-02-25') TO ('2024-02-26');
CREATE TABLE transactions_2024_02_26 PARTITION OF transactions FOR VALUES FROM ('2024-02-26') TO ('2024-02-27');
CREATE TABLE transactions_2024_02_27 PARTITION OF transactions FOR VALUES FROM ('2024-02-27') TO ('2024-02-28');
CREATE TABLE transactions_2024_02_28 PARTITION OF transactions FOR VALUES FROM ('2024-02-28') TO ('2024-02-29');
CREATE TABLE transactions_2024_02_29 PARTITION OF transactions FOR VALUES FROM ('2024-02-29') TO ('2024-03-01');
CREATE TABLE transactions_max PARTITION OF transactions FOR VALUES FROM ('2024-03-01') TO (MAXVALUE);

INSERT INTO transactions (transaction_time, account_id, transaction_location, transaction_amount)
SELECT
    TIMESTAMP '2024-01-01 00:00:00' + (interval '0.01 second' * (generate_series(1, 300000000) - 1)),
    (random() * 3000000)::int + 1 AS account_id,
    generate_series(1, 300000000) AS transaction_location,
    generate_series(1, 300000000) AS transaction_amount;

---------------------------------------------------- composite index

-- CREATE INDEX idx_transactions_time_account ON transactions (transaction_time, account_id);

EXPLAIN ANALYZE -- 2800ms -> 1409ms
SELECT *
FROM transactions
WHERE
    account_id = 2000000 and
    '2024-01-20 00:00:00' <= transaction_time and
    transaction_time < '2024-01-27 00:00:00';

-- DROP INDEX idx_transactions_time_account;

---------------------------------------------------- index 수정

CREATE INDEX idx_transactions_account_id ON transactions (account_id);

EXPLAIN ANALYZE -- 10ms -> 0.2 ~ -0.3ms
SELECT *
FROM transactions
WHERE
    account_id = 2000000 and
    '2024-01-20 00:00:00' <= transaction_time and
    transaction_time < '2024-01-27 00:00:00';

-- DROP INDEX idx_transactions_account_id;


CREATE INDEX idx_trantions_account_time ON trans (account_id, transaction_time);

EXPLAIN ANALYZE -- 4221.571 ms -> 0.2 ~ -0.3ms
SELECT *
FROM transactions
WHERE
    account_id = 20000 and
    '2024-01-20 00:00:00' <= transaction_time and
    transaction_time < '2024-01-27 00:00:00';




---------------------------------------------------- index (Hash)

CREATE INDEX idx_transactions_account_id ON transactions USING HASH (account_id);

EXPLAIN ANALYZE -- 2~10ms -> 0.2 ~ 0.3ms
SELECT *
FROM transactions
WHERE
    account_id = 2000000 and
    '2024-01-20 00:00:00' <= transaction_time and
    transaction_time < '2024-01-27 00:00:00';


-- DROP INDEX idx_transactions_account_id;

---------------------------------------------------- id index (B-tree)

CREATE INDEX idx_transactions_id ON transactions (id);

EXPLAIN ANALYZE -- 14ms -> 1ms
SELECT *
FROM transactions
WHERE id = 100000000;

EXPLAIN ANALYZE -- 8ms -> 1ms
SELECT *
FROM transactions
WHERE id = 200000000;

EXPLAIN ANALYZE -- 4ms -> 1ms
SELECT *
FROM transactions
WHERE id = 300000000;

-- DROP INDEX idx_transactions_id;

---------------------------------------------------- id in5~dex (Hash)

CREATE INDEX idx_transactions_id ON transactions USING HASH (id);

EXPLAIN ANALYZE -- 28ms -> 1ms
SELECT *
FROM transactions
WHERE id = 100000000;

EXPLAIN ANALYZE -- 8ms -> 1ms
SELECT *
FROM transactions
WHERE id = 200000000;

EXPLAIN ANALYZE -- 9ms -> 1ms
SELECT *
FROM transactions
WHERE id = 300000000;

-- DROP INDEX idx_transactions_id;

---------------------------------------------------- without partition

CREATE TABLE trans (
    id BIGINT GENERATED ALWAYS AS IDENTITY,
    transaction_time TIMESTAMP NOT NULL,
    account_id BIGINT NOT NULL,
    transaction_location BIGINT NOT NULL,
    transaction_amount NUMERIC NOT NULL
);

INSERT INTO trans (transaction_time, account_id, transaction_location, transaction_amount)
SELECT
    TIMESTAMP '2024-01-01 00:00:00' + (interval '0.01 second' * (generate_series(1, 300000000) - 1)),
    (random() * 3000000)::int + 1 AS account_id,
    generate_series(1, 300000000) AS transaction_location,
    generate_series(1, 300000000) AS transaction_amount;

---------------------------------------------------- composite index

CREATE INDEX idx_trans_time_account ON trans (transaction_time, account_id);

EXPLAIN ANALYZE -- 2479ms
SELECT *
FROM trans
WHERE
    account_id = 1000000 and
    '2024-01-20 00:00:00' <= transaction_time and
    transaction_time < '2024-01-27 00:00:00';

-- DROP INDEX idx_trans_time_account;

                                                                            QUERY PLAN
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Index Scan using idx_trans_time_account on trans  (cost=0.57..1654318.22 rows=18 width=40) (actual time=255.848..2478.683 rows=17 loops=1)
   Index Cond: ((transaction_time >= '2024-01-20 00:00:00'::timestamp without time zone) AND (transaction_time < '2024-01-27 00:00:00'::timestamp without time zone) AND (account_id = 2000000))
 Planning Time: 2.752 ms
 Execution Time: 2479.048 ms
(4 rows)


------------------------

CREATE INDEX idx_trans_time_account ON trans (account_id, transaction_time);

EXPLAIN ANALYZE -- 6ms -> 0.1ms
SELECT *
FROM trans
WHERE
    account_id = 2000000 and
    '2024-01-20 00:00:00' <= transaction_time and
    transaction_time < '2024-01-27 00:00:00';

-- DROP INDEX idx_trans_time_account;

---------------------------------------------------- index 수정

CREATE INDEX idx_trans_account ON trans (account_id);

EXPLAIN ANALYZE -- 20ms
SELECT *
FROM trans
WHERE
    account_id = 2000000 and
    '2024-01-20 00:00:00' <= transaction_time and
    transaction_time < '2024-01-27 00:00:00';

-- DROP INDEX idx_trans_account_id;

----------------------------------------------------

CREATE INDEX idx_trans_time ON transactions (transaction_time);
CREATE INDEX idx_trans_account ON trans (account_id);

EXPLAIN ANALYZE -- 20ms
SELECT *
FROM trans
WHERE
    account_id = 2000000 and
    '2024-01-20 00:00:00' <= transaction_time and
    transaction_time < '2024-01-27 00:00:00';

-- DROP INDEX idx_trans_time;
-- DROP INDEX idx_trans_account;
                                                                            QUERY PLAN
------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Index Scan using idx_trans_account on trans  (cost=0.57..374.63 rows=18 width=40) (actual time=9.307..19.519 rows=17 loops=1)
   Index Cond: (account_id = 2000000)
   Filter: (('2024-01-20 00:00:00'::timestamp without time zone <= transaction_time) AND (transaction_time < '2024-01-27 00:00:00'::timestamp without time zone))
   Rows Removed by Filter: 69
 Planning Time: 2.800 ms
 Execution Time: 19.581 ms
(6 rows)