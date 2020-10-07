import sqlite3

def delete_b():
    conn=sqlite3.connect("C:/Users/Yoo/AppData/Local/Programs/Python/Python38-32/testdb.db")
    cur=conn.cursor()
    del_sql='delete from test where title=?'
    cur.execute(del_sql,('중국사',))
    conn.commit()
    conn.close()

delete_b()
