import sqlite3
conn = sqlite3.connect("database.db", check_same_thread=False)
cursor = conn.cursor()

# 创建用户表
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE,
        pwd TEXT,
        tel TEXT
    )
"""
)
conn.commit()
