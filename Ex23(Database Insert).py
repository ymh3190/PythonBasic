import sqlite3

"""
insert : DB에 값을 넣는 것
select : 넣은 값을 확인하는 것
"""

def insert_b():
    conn=sqlite3.connect("C:/Users/Yoo/AppData/Local/Programs/Python/Python38-32/testdb.db")
    cur=conn.cursor()
    """
    #1. insert 첫번째 방법 - 값이 정해진 쿼리라고 해서 정적쿼리라 칭한다.
    insert into 테이블명 values(필드를 명시하지 않으면 순서대로 값이 저장된다.)
    """
    cur.execute("insert into test values('개발자의 코드','2016-05-26','a',200,0)")

    """
    #2. insert 두번째 방법 - 값이 동적인 쿼리라고 해서 동적쿼리라 칭한다.
    insert into test values(?,?,?,?,?)
    """
    ins_sql='insert into test values(?,?,?,?,?)'
    cur.execute(ins_sql,('클린코드','2016-04-04','b',300,1)) #여기서 쿼리가 정해진다.

    """
    #3. insert 세번째 방법 - 여러 개를 넣을 때
    리스트형태 안에 튜플로 값을 넣는다.
    """
    books=[('한국사','2016-02-02','c',330,1),('물리개론','2015-01-04','a',130,0),
           ('건축사','2013-10-14','e',150,0)]
    cur.executemany(ins_sql,books)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    insert_b()

