"""
클래스 상속
"""
"""
class Up:
    c=30
    def __init__(self):
        self.a=5
        self.b=10

class Low(Up):
    pass

low1=Low()
print(low1.a)
print(low1.b)
print(low1.c)
print(Up.c) #클래스 변수는 클래스이름으로 바로접근해도 된다.
"""

"""
class Up:
    c=30
    def __init__(self):
        self.a=5
        self.b=10

class Low(Up):
    c=130
    def __init__(self):
        self.a=105
        self.b=110

low1=Low()
print(low1.a)
print(low1.b)
print(low1.c)
"""

"""
class Up:
    c=30
    def __init__(self):
        self.a=5
        self.b=10

class Low(Up):
    c=130
    def __init__(self):
        #self.a=105

        #파이썬에서는 자식객체에 없는 부모클래스의 객체를 사용하려면
        #부모의 초기자를 명시적으로 초기화해야한다.
        
        self.b=110
        super().__init__()
        
low1=Low()
print(low1.a)
print(low1.b)
print(low1.c)
"""

"""
class Up:
    def aaa():
        print('aaa')
    def bbb(self):
        print('bbb')

class Low(Up):
    pass

low1=Low()
Up.aaa()
low1.bbb()
"""

class Up:
    def aaa():
        print('aaa')
    def bbb(self):
        print('bbb')

class Low(Up):
    def aaa():
        print('aaa_2')
    def bbb(self):
        print('bbb_2')

Up.aaa()
Low.aaa()
up1=Up()
up1.bbb()
low1=Low()
low1.bbb()









