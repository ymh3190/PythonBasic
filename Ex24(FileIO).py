"""
1) 파일 쓰기 'w' (write)
"""
#f=open('C:/Users/Yoo/AppData/Local/Programs/Python/Python38-32/data/test.txt','w')
#f.write('안녕하세요!!')
#f.flush() # 내용을 파일로 전송한다. 즉, 버퍼를 비운다.
#f.close()

"""
2) 파일 읽기 'rt' (read text)
"""
#f=open('C:/Users/Yoo/AppData/Local/Programs/Python/Python38-32/data/test.txt','rt')
#print(f.readline()) #한줄씩 읽어온다.
"""
여러 줄을 읽기 - 1
for i in range(2):
    print(f.readline())
"""

"""
여러 줄을 읽기 - 2
for i in f:
    print(i)

"""

"""
for i in f:
    print(i, end='') #한줄 띄우기 방지
"""

"""
리스트 : 여러 줄을 읽기 - 3
r=list(f)
print(r[:3])
"""

"""
#자주 쓰는 with open(str) as str:
#with를 쓰면 close까지 함께 실행된다.
with open('C:/Users/Yoo/AppData/Local/Programs/Python/Python38-32/data/test.txt','rt') as f:
    f_list=f.readlines() #들여쓰기 해야됨
print(f_list)

print(f.closed) #현재 파일 객체가 열렸는지 닫혔는지 확인
"""

"""
파일모드
r -> 읽기
w -> 쓰기
a -> 추가
"""

#f=open('C:/Users/Yoo/AppData/Local/Programs/Python/Python38-32/data/test.txt','w')
"""
for i in range(1,8):
    msg=f'{i}번째\n'
    f.write(msg)
f.close()
"""

"""
for i in range(1,8):
    f.write('%d번째\n'%i)
f.close()

"""


#f=open('C:/Users/Yoo/AppData/Local/Programs/Python/Python38-32/data/test.txt','r')
"""
while True:
    line=f.readline()
    if not line:
        print(type(line))
        break
    print(line)
f.close()
"""

"""
line=f.readlines()
print(type(line))
for i in line:
    print(i)
f.close()
"""

"""
#read()함수
line=f.read()
print(type(line))
print(line)
f.close()
"""



























