"""
함수와 모듈
"""

"""
1) 함수 정의하기
def 함수이름(매개변수):
    실행코드
    (return) return값이 있으면 작성하고 없으면 생략가능
"""




import Ex13CalcModule as c
from Ex13CalcModule import sub
import Ex13CalcModule
def add():
    a = 7
    b = 8
    print(a+b)


def pro():
    print('*'*20)


def min(a, b):
    print(a-b)


def mul(a, b):
    return a*b


"""
2) 함수 사용하기
"""
add()
pro()
min(77, 50)
print(mul(10, 40))

"""
3) 모듈 만들기
모듈의 개념은 관련있는 여러 개의 함수를 모아둔 것
~~~.py 파이썬 파일 만들어서 필요한 함수 작성하
"""

"""
4) 모듈 사용하기
import modu
a=modu.func(7)
print a
"""


s = Ex13CalcModule.mul(7, 8)
print(s)
s = Ex13CalcModule.sub(7, 8)
print(s)
print()

"""
5) 모듈 편리하게 사용하기
매번 모듈이름을 쓰니 불편하다.
from modu import * (모듈안에 있는 함수를 다 쓰겠다)
from modu import sub (특정함수 sub만 쓰겠다)
import modu as c (모듈이름 대신 c라는 문자로 대신 쓰겠다)
"""
s = sub(7, 8)
print(s)
s = mul(7, 8)
print(s)
print()

s = c.sub(7, 8)
print(s)
s = c.mul(7, 8)
print(s)
