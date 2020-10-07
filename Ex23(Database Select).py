"""
1) 전체 데이터 가지고 오기
"""

"""
import sqlite3

def select_b():
    conn=sqlite3.connect("C:/Users/Yoo/AppData/Local/Programs/Python/Python38-32/testdb.db")
    cur=conn.cursor()
    # test라는 테이블로부터 *(모든필드)를 다 보여주겠다
    cur.execute('select * from test')
    print('[1] 전체 데이터 출력하기')

    #1. fetchall : 테이블에 있는 모든 데이터를 다 가져오겠다.
    #2. rs : 리스트형태
    rs=cur.fetchall()
    
    for book in rs:
        print(book)
        
    conn.close()

if __name__ == "__main__":
    select_b()
"""


"""
2) 특정 조건에 해당하는 것만 불러오기
"""


import sqlite3

def select_b(number):
    conn=sqlite3.connect("C:/Users/Yoo/AppData/Local/Programs/Python/Python38-32/testdb.db")
    cur=conn.cursor()
    cur.execute('select * from test where title="한국사"')
    print('[2] 일부 데이터 출력하기')
    rs=cur.fetchmany(number) # number수에 따라 가져오기
    for book in rs:
        print(book)
    conn.close()

if __name__ == '__main__':
    select_b(1)


