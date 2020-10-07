import sqlite3

def update_b():
    conn=sqlite3.connect("C:/Users/Yoo/AppData/Local/Programs/Python/Python38-32/testdb.db")
    cur=conn.cursor()

    """
    1. SQLite문법 : update 테이블 set 열이름=변경할값(동적or정적) where=조건
    """
    up_sql='update test set title=? where title=?'
    cur.execute(up_sql, ('중국사','한국사'))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    update_b()
