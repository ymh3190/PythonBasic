"""
파이썬 함수 익히기
"""
#1. 함수를 이용해서 단을 입력받아 해당 단의 구구단을 출력하는 프로그램을 작성
"""
def func1():
    i=input('단을 입력하세요. ')
    return int(i)

#a=func1()
for i in range(1,10):
    pass
    #b=int(a)*i
    #print(a + '*' + str(i) + '=' + str(b))
    #print(a,' * ',i,' = ',a*i)

def my_fun():
    dan=int(input('단을 입력하세요! : '))
    for i in range(1,10):
        print(dan,'*',i,'=',dan*i)

#my_fun()
"""

#2. 숫자 2개를 입력받아 사이 숫자들의 합을 구하시오.(함수이용)
"""
너무 어려운데?
"""
"""
def my_fun():
    start=int(input('시작 값 : '))
    end=int(input('끝 값 : '))
    sum=0
    for i in range(start,end+1):
        sum+=i

    print('합계 = ',sum)

#my_fun()

def func2():
    a=input('시작 값 : ')
    b=input('끝 값 : ')
    return [int(a),int(b)]

li=func2()
sum=0
for i in range(li[0],li[-1]+1):
    sum+=i
#print('합계 = ',sum)
"""

#3. 입력한 숫자만큼 별을 출력하세요.(함수이용)
"""
def func3():
    i=input('숫자 입력 ')
    print('*'*int(i),end='')

#func3()

def func3_1():
    i=input('숫자 입력 ')
    return '*'*int(i)
msg=func3_1()
print(msg)
"""

#4. 숫자 2개를 입력해서 큰 값을 출력하세요.(함수와 return사용)
"""
def func4():
    input1=int(input('첫번째 숫자 '))
    input2=int(input('두번째 숫자 '))
    return input1,input2

input_li=func4()
if input_li[0] > input_li[-1]:
    print(input_li[0])
elif input_li[0] == input_li[-1]:
    print()
elif input_li[0] < input_li[-1]:
    print(input_li[-1])
"""

#5. 숫자 3개를 입력해서 가장 큰 값을 출력하세요.(함수와 return 사용)
"""
def func5():
    input1=int(input('첫번째 숫자 '))
    input2=int(input('두번째 숫자 '))
    input3=int(input('세번째 숫자 '))
    input_li=[input1,input2,input3]
    if input_li[0]>input_li[1]:
        del input_li[1]
        if input_li[0]>input_li[1]:
            del input_li[1]
        else:
            del input_li[0]
        print(input_li[0])
    else:
        del input_li[0]
        if input_li[0] < input_li[1]:
            del input_li[0]
        else:
            del input_li[1]
        print(input_li[0])

#func5()
        
def my_fuc(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
input1=int(input('첫번째 숫자 '))
input2=int(input('두번째 숫자 '))
input3=int(input('세번째 숫자 '))
print(my_fuc(input1,input2,input3))
"""

