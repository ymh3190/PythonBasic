"""
1) 상속
"""

"""
class Point:
    def __init__(self):
        self.x=int(input('x=?'))
        self.y=int(input('y=?'))
    def disp(self):
        pass

class Circle(Point):
    def __init__(self):
        super().__init__()
        self.r=int(input('r=?'))
    def disp(self):
        print('원',self.x,self.y,self.r)

class Rect(Point):
    def __init__(self):
        super().__init__()
        self.w=int(input('w=?'))
        self.h=int(input('h=?'))
    def disp(self):
        print('사각형',self.x,self.y,self.w,self.h)

def main():
    li=[]
    while True:
        s=input('도형종류(1. 사각형, 2. 원, 3. 조회, 4. 종료) ?')
        if s=='1':
            li.append(Rect())
        elif s=='2':
            li.append(Circle())
        elif s=='3':
            for i in li:
                i.disp()
        elif s=='4':
            break
        else:
            print('잘못된 입력입니다.')
    print('프로그램을 종료합니다.')
    
main()
"""

"""
문제) 상속과 다형성 사진 참고
"""


















            
