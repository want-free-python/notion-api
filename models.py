import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# 페이지 테이블 생성
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pages (
        id INTEGER PRIMARY KEY,
        title TEXT,
        content TEXT,
        parent_id INTEGER,
        FOREIGN KEY (parent_id) REFERENCES pages(id)
    )
''')
conn.commit()


