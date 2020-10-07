"""
DB활용 예제
"""

import sqlite3

class Db:
    conn=None
    cur=None

    def getConn():
        Db.conn=sqlite3.connect("C:/Users/Yoo/AppData/Local/Programs/Python/Python38-32/phone.db")
        Db.cur=Db.conn.cursor()

    def endConn():
        Db.conn.commit()
        Db.conn.close()

    def createtable():
        Db.cur.execute('create table tell(name text, no text)')

    def insert():
        name=input('이름?')
        no=input('전화번호?')
        sql='insert into tell values(?,?)'
        Db.cur.execute(sql,(name,no))

    def select():
        sql='select * from tell'
        Db.cur.execute(sql)
        rs=Db.cur.fetchall()
        print('*****데이터 출력*****')
        for k,v in rs:
            print(k,v)

    def delete():
        name=input('이름?')
        sql='delete from tell where name=?'
        Db.cur.execute(sql,(name,))

    def update():
        name=input('이름?')
        no=input('번호?')
        sql='update tell set no=? where name=?'
        Db.cur.execute(sql,(no,name))

Db.getConn()

while True:
    n=input('a. 테이블생성 1. 입력 2. 조회 3. 삭제 4. 수정 0. 종료')
    if n=='a':
        Db.createtable()
    elif n=='1':
        Db.insert()
    elif n=='2':
        Db.select()
    elif n=='3':
        Db.delete()
    elif n=='4':
        Db.update()
    elif n=='0':
        Db.endConn()
        break
print('프로그램을 종료합니다.')