"""
1) range()함수
range(값) : 0부터 값-1
range(시작값,end-1)
list(range(시작,end-1,증감))
"""
list(range(5))
list(range(1,5))
list(range(1,11))
list(range(1,11,2))

for i in range(1,11):
    print(i)

for i in range(10):
    print(i)
for i in range(10):
    print('안녕하세요')

"""
이중for문
"""
for i in range(7):
    for j in range(7):
        print('*',end='')
    print('\n')
    
for i in range(2,10):
    for j in range(1,10):
        print(str(i) + ' * ' + str(j) + ' = ' + str(i*j))

for i in range(2,10,2):
    for j in range(1,10):
        print(str(i) + ' * ' + str(j) + ' = ' + str(i*j))

for i in range(1,6):
    print('*' * i)

for i in range(1,6):
    print(' ' * (5-i) + '*'*i)
        
for i in range(5):
    for j in range(0,i+1):
        print('*',end='')
    print()
