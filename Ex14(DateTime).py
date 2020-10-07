import datetime

y={0:'월', 1:'화', 2:'수', 3:'목', 4:'금', 5:'토', 6:'일'}

#date
d=datetime.date(2020,9,15)
print(d)
print(d.weekday())
print(y[d.weekday()])

d=datetime.date.today()
print(d)
print(y[d.weekday()])
"""
#에러 date에는 now함수가 없다.
d=datetime.date.now()
"""
print(d)

#datetime
d=datetime.datetime(2018,4,10,12,32,37) #datetime모듈에 datetime클래스?
print(d)

#time
d=datetime.time(12,32,37)
print(d)

d=datetime.datetime.now()
print(d)
d=datetime.datetime.today()
print(d)

"""
문제
"""
#1. 오늘날짜 중 연도만 출력하세요.
from datetime import date
"""
datetime.date.today() -> date.today()로 줄일 수 있다
"""
d=date.today()
print(d.year)

#2. 오늘날짜와 2일을 출력하세요.
from datetime import timedelta
from datetime import date

t=timedelta(days=2)
d=date.today()
print(d)
print(t)

#3. 오늘날짜로부터 2745일이 지나면 몇년 몇월 몇일 일까요?
from datetime import date
from datetime import timedelta

d=date.today()
t=timedelta(days=2745)
print(d+t)

#4. 2027년 11월 12일까지는 몇일 남았을까요?
from datetime import date
d=date.today()
d2=date(2020,11,12)
print(d2-d)

#5. 시간을 설정하고 출력하세요.
from datetime import time
d=time(11,20,10)
print(d)

#6. 시간을 설정하고 시,분,초를 출력하세요.
from datetime import time
d=time(11,20,10)
print(d.hour)
print(d.minute)
print(d.second)

#7. 날짜와 시간을 설정하고 출력하세요.
import datetime
d=datetime.datetime(2016,12,24,11,20,10,50)
print(d.year)
print(d.month)
print(d.day)
print(d.hour)
print(d.minute)
print(d.second)
print(d.microsecond)



