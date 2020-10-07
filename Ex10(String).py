"""
문자열
"""
#1. 나이
ju='801213-1674523'
yy=int(ju[0:2])
age = 2020 -(1900 + yy) +1
print(age)

#2. 월
mm=ju[2:4]
print(mm+'월')

#3. 일
dd=ju[4:6]
print(dd+'일')

print(ju[7])
#4. 성별
if int(ju[7])%2==0 :
    print('여자')
else :
    print('남자')

ju='061213-4674523'
if ju[7] in ('1','2') : print(1900)
else : print(2000)

s='1-2-3-4-5-6-7-8-9'
li=s.split('-')
tot=0
for i in li: #for문의 범위가 리스트라면, 인자는 리스트요소를 순회한다.
    tot+=int(i)
print(tot)
