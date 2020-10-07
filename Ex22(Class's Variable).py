"""
1) 클래스 변수
"""
class Person:
    a=0
    def __init__(self):
        Person.a+=1 #Person.a
    def disp(self):
        print(Person.a)

#Person.a : 클래스 변수는 클래스이름으로 접근한다.
"""
p1=Person()
print(p1.a)
p2=Person()
print(p2.a)
"""

"""
2) 인스턴스 변수
"""
class Person:
    def __init__(self):
        self.a=0 #self.a
        self.a+=1
    def disp(self):
        print(self.a)
#self.a : self.a는 인스턴스 변수이고, self로 접근한다.
#객체마다 각각의 값을 유지할 수 있다.
"""
p1=Person()
p1.disp()
p2=Person()
print(p2.a)
p3=Person()
print(p3.a)
"""

"""
3) 클래스 변수(가족 공통의 냉장고)
구성원끼리 공유할지?
"""
class Person:
    li=[]
    def __init__(self,a):
        Person.li.append(a)
    def disp(self):
        print(Person.li)
"""
p1=Person('우유')
p1.disp()
p2=Person('콜라')
p2.disp()
p3=Person('주스')
p3.disp()
"""

"""
4) 인스턴스 변수(각 개인의 냉장고)
구성원끼리 공유 안할지?
"""
class Person:
    def __init__(self,a):
        self.li=[]
        self.li.append(a)
    def disp(self):
        print(self.li)
"""
p1=Person('우유')
p1.disp()
p2=Person('콜라')
p2.disp()
p3=Person('주스')
p3.disp()
"""

"""
5) 혼동하기 쉬운 예제
"""
class Person:
    a=5 #클래스 변수
    def __init__(self,a):
        self.a=a #인스턴스 변수
        #클래스 변수에 사용하려면 Person.a로 접근
    def disp(self):
        print(self.a)
"""
p1=Person(5)
p1.disp()
p2=Person(10)
p2.disp()
p3=Person(15)
p3.disp()
"""

class Person:
    a=5 #클래스 변수는 있지만
    def __init__(self,a):
        pass #인스턴스 변수는 없다.
    def disp(self):
        print(self.a) #인스턴스 변수를 출력해라.
"""
p1=Person(5)
p1.disp()
p2=Person(10)
p2.disp()
p3=Person(15)
p3.disp()
"""

















