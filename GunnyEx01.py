#프린트함수
print("hello world")

#파이썬에서는 세미콜론이 없다. 변수타입이 없다.
a = 1
print(type(a)) #a타입 출력

a="helloworld"  
print(type(a)) #a타입 출력

#리스트 생성
li = []
li[:] = a
li.sort()
print(li)

#구글에 python string methods로 검색하면 스트링관련 함수가 있다.

print(a.upper()) #대문자 출력

#조건문에 괄호가 빠짐
a = 5

if a > 3 :
    print("hello")

#파이썬의 가장 큰 장점 - 풍부한 라이브러리
#사용법은
#1. 검색 ex) 수학관련 라이브러리를 찾는다면 -> python numeric library -> 필요한 함수(numpy)를 찾는다.
#2. 다운 ex) cmd에서 pip install numpy 명령어를 실행한다.
#3. 사용

import numpy

a = numpy.arange(10).reshape(2,5)

print(a)

#이미지 관련 작업을 하고싶다면? -> python image processing library


    


