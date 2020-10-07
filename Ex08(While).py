"""
1) while
while 조건:
    실행코드
"""
c=1
while c<=10:
    print(c)
    c+=1

"""
2) 무한루프
"""
#ex1
while True:
    score=int(input('점수? '))
    if score>=0 and score<=100:
        break
print(score)

#ex2
while 1:
    i=input('입력? ')
    if len(i)==4:
        break;
    
print(i)
