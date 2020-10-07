"""
1) 클래스 만드는 법

class Person: #Person
    def __init__(self,name,age): #__init__, self
        self.name=name
        self.age=age

cf) 클래스안의 함수를 메소드라 부른다.
#Person : 클래스의 이름은 첫글자를 대문자로 한다.
#__init__ : 초기자라 부르며, C++에서 생성자와 같다.
#self : C++에서 this와 같다.
        함수의 매개변수에 self가 붙으면 메소드 아니면 함수라 부른다.
"""

"""
2) 클래스 객체 할당

p1=Person('홍길동',22)
p2=Person('김철수',32)

"""
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=Person('홍길동',22)
p2=Person('김철수',32)

"""
3) 클래스 객체 접근
"""
#하지만 보안상의 이유로 아래와 같이 접근하지 않는다.
"""
print(p1.name)
print(p2.name)
print(p1.age)
print(p2.age)
"""

"""
4) 클래스 객체 접근 2번째
"""
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def disp(self):
        print(self.name)
        print(self.age)
"""
p1=Person('홍길동',22)
p2=Person('김철수',32)
p1.disp()
p2.disp()
"""

"""
5) 클래스 객체 접근 3번째
"""
class Person:
    def __init__(self):
        self.name=input('이름:')
        self.age=int(input('나이:'))
    def disp(self):
        print(self.name)
        print(self.age)
"""
p1=Person()
p2=Person()
p1.disp()
p2.disp()
"""

"""
6) 사람이 2명이면 저렇게 처리한다 하지만, 100명,1000명이면 어떻게 할래?
"""
class Person:
    def __init__(self):
        self.name=input('이름:')
        self.age=int(input('나이:'))
    def disp(self):
        print(self.name)
        print(self.age)

#해결책은 리스트
li=[]
for i in range(3): #range안에 숫자가 인원 수를 의미한다.
    li.append(Person())
for i in li: #li대신에 range(len(li))
    i.disp() #i 대신에 li[i]
    





















