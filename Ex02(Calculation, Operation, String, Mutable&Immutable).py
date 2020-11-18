# 덧셈
print(5+6)

# 곱셈
print(11*-3)

# 나누기
print(5/3)

# 몫
print(5//3)

# 나머지
print(5 % 3)

# 제곱
print(3**2)
print(3**3)

# 비교연산자
"""
>, <, >=, <=, !=, ==
"""
print(15+9 == 24)

# 논리연산자
"""
and, or
"""
print(2 > 3 or 3 < 5)
print(2 > 3 and 3 < 5)

# 문자열
print('1234567')
print("1234567")
print("abcd\nefg")

print("""
123
456
789
""")

# 문자열관련함수
print(len("abcdefg"))
print(len('홍길동'))

name = 'swplay'
var1 = '재미있는 파이썬공부'
print(var1.replace('공부', 'study'))
print(name.upper())  # 대문자로 변환
var2 = 'ABC'
print(var2.lower())

a = 10
b = '10'
print(a)
print(type(a))
print(b)
print(type(b))

print(a+int(b))
print(str(a)+b)

#Mutable & Immutable
"""
파이썬에는 변할 수 있는 데이터형과 아닌 것이 있다.
Mutable : list(리스트형), dict(사전형), set(집합형), byte array(바이트 배열형)
Immutable : numbers(정수,실수,복소수형), string(문자열형), tuple(튜플형),
            frozenset(불변집합형), bytes(바이트형)
"""
