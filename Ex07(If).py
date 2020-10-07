""""
제어문(if문)
다른 언어와 비슷하게 if문, for문, while문, continue문이 있지만
문법적 요소가 조금 다르다.
"""

"""
1) if
if 조건:
    실행코드
"""
age=34
if age>12:
    print('ok')
    print('ok2')

"""
2) if-else
if 조건:
    실행코드
else:
    실행코드
"""
if age>42:
    print('참')
else:
    print('거짓')

"""
3) if-elif-else
if 조건:
    실행코드
elif 조건:
    실행코드
else:
    실행코드
"""
age=int(input('몇살?'))
if age<8:
    print('유아')
elif age>=8 and age<20:
    print('청소년')
else:
    print('성인')

"""
4) 중첩 if
"""
k=int(input('구분: 1. 주간 2. 야간 ?'))
m=int(input('대상: 1. 대인 2. 소인 ?'))
if k==1: #주간
    if m==1: #대인
        y=40000
    else: #소인
        y=30000
else: #야간
    if m==1: #대인
        y=28000
    else: #소인
        y=20000
print(y)
