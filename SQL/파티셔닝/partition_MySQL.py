import mysql.connector
from datetime import datetime, timedelta
import random

# MySQL 연결 설정
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)
mycursor = mydb.cursor()

s = set(i*100_000 for i in range(3000))

# 데이터 삽입
start_time = datetime(2024, 1, 1)
data_to_insert = []
for i in range(300000000):
    transaction_time = start_time + timedelta(seconds=i*0.01)
    account_id = random.randint(1, 3000000)
    transaction_location = i + 1
    transaction_amount = i + 1
    data_to_insert.append((transaction_time, account_id, transaction_location, transaction_amount))
    if i in s:
        print(i)
    if len(data_to_insert) == 1000:  # 적절한 일괄 크기 선택
        sql = """
        INSERT INTO
        transactions_2 (transaction_time, account_id, transaction_location, transaction_amount)
        VALUES (%s, %s, %s, %s)
        """
        mycursor.executemany(sql, data_to_insert)
        data_to_insert = []

# 남은 데이터 삽입
if data_to_insert:
    sql = """
    INSERT INTO
    transactions_2 (transaction_time, account_id, transaction_location, transaction_amount)
    VALUES (%s, %s, %s, %s)
    """
    mycursor.executemany(sql, data_to_insert)

# 변경사항 커밋
mydb.commit()

# 연결 종료
mydb.close()
