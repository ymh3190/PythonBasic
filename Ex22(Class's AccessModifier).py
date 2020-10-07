"""
접근제한자
"""
class Test:
    def __init__(self):
        self.a=5
        self.b=10
        self.__c=20 # private
    def disp(self):
        print(self.a)
        print(self.b)
        print(self.__c)

#t=Test()
#t.disp()

class Test2(Test):
    def disp(self):
        print(self.a)
        print(self.b)
        #print(self.__c)

t=Test2()
t.disp()
