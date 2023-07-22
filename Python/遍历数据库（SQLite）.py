import sqlite3 as sql
conf = {}
# 连接至数据库
conn = sql.connect("db/config.db")
cursor = conn.cursor()
# 获取所以value

cursor.execute("SELECT * FROM config;")
rows = cursor.fetchall()

# 遍历数据
for row in rows:
    # 每行数据以元组形式返回。
    key = row[0]
    value = row[1]
    # 进行相应的操作，这里仅打印出数据
    conf[key] = value
