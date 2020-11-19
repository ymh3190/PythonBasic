"""
파이썬의 장점 활용하기
"""

# 1. 변수값 교환(Swap)
import random
a = 7
b = 5
a, b = b, a
print(a)
print(b)

a = 7
b = 5
c = 9
a, b, c = c, a, b
print(a)
print(b)
print(c)

# 2. 중복값 제거
mylist = [1, 5, 2, 5, 1, 12, 2]
print(mylist)
print(dict().fromkeys(mylist).keys())
k = list(dict().fromkeys(mylist).keys())
print(k)

# 3. 랜덤모듈

print(random.choice([1, 2, 3, 4, 5, 6]))
k = ('가', '나', '다')
print(random.choice(k))

li = ['원숭이', '닭', '개', '돼지', '쥐', '소', '호랑이', '토끼', '용', '뱀', '말', '양']
li2 = random.sample(range(1, 13), 5)  # 1~13의 숫자중에서 5개 무작위로 뽑기
for i in li2:
    print(li[i-1])

li2 = random.sample(li, 3)
for i in li2:
    print(i)


li2 = random.sample(range(1, 6), 5)
for i in li2:
    print(i)
