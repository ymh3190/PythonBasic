"""
파이썬의 데이터베이스
데이터베이스에서는 여러가지를 붙여서 쓸 수 있다.
파이썬에서 기본적으로 깔려있는 프로그램이 sqlite3 모듈
sqlite를 이용해서 테이플생성하기
"""

"""
SQLite는 MySQL나 PostgreSQL와 같은 데이터베이스 관리 시스템이지만,
서버가 아니라 응용 프로그램에 넣어 사용하는 비교적 가벼운 데이터베이스이다

우선 SQLite Browser를 다운받는다.
"""

import sqlite3

def create_table():
    #sqlite3.connect("C:\Users\Yoo\AppData\Local\Programs\Python\Python38-32/testdb.db")
    #\는 2개씩 써야하고, /는 하나만 쓰면된다.
    conn=sqlite3.connect("C:/Users/Yoo/AppData/Local/Programs/Python/Python38-32/testdb.db")
    cur=conn.cursor() #connect로 db에 접속했으면, db를 관리하기 위해 cursor()를 호출
    """
    1. SQL Query문은 따로 공부해야한다.
    2. create table test : test이름의 테이블을 생성한다.
    3. 변수는 title text, pubd text, pus text, page integer, re integer
    4. title(책제목) text(자료형)는 string으로 생각
    5. pubd(출판일) text
    6. pus(출판사)
    7. page(페이지) integer(정수)
    8. re(추천수)
    """
    cur.execute('''
    create table test(title text,
    pubd text,
    pus text,
    page integer,
    re integer)
    ''')
    """
    1. commit : 최종적으로 반영하겠다.
    2. rollback : 취소하겠다.
    3. 이렇게 커밋과 롤백하는 것을 transaction 처리라고 한다.
    4. transaction : 데이터베이스 상태를 변화시키기 위해 수행하는 작업을 뜻한다.
    """
    conn.commit()
    conn.close() #반드시 connect를 close해야한다.
    """
    이까지 마쳤으면 데이터베이스 파일이 생성됐을텐데 제대로 생성됐는지 확인하기 위해
    DB Browser를 열고 1. open database
    """

if __name__=="__main__": #__name__=="__main__"
    create_table()

#__name__=="__main__" : 이 프로그램을 서브로 실행시켰을 땐 동작하지않고
#                       반드시 main으로 실행시켰을 때만 테이블을 만들겠다는 코드