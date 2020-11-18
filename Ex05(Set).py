"""
1) set의 특징
1.1 딕셔너리에서 값을 제거한 키와 비슷한 원리다.
1.2 중괄호{}로 값을 구분한다.
1.3 순서대로 저장되지 않는다.
1.4 중복된 값은 한 번만 저장된다.
"""
b = {2, 4, 6, 8}
print(b)  # 1.3

b = {2, 4, 2, 1, 2, 3}
print(b)  # 1.4

dic = {'kor': 80, 'eng': 90, 'mat': 77}
print(dic)
a = set(dic)  # 1.1 딕셔너리를 set에 넣으면 key만 들어간
print(a)

"""
2) set 생성하기
ex) a = set()
초기화시 반드시 set()함수를 이용한다.
"""
a = set()
print(type(a))
a = {}
print(a)
print(type(a))

"""
3) in으로 값 찾기
"""
dic = {'경상도': {'부산', '대구', '울산', '공통'}, '전라도': {'광주', '전주', '공통'}}
print(dic)

# Key와 Value
for name, contents in dic.items():
    if '광주' in contents:
        print(name+'\n')

for name, contents in dic.items():
    if '공통' in contents and not ('대구' in contents):
        print(name+'\n')

# Key
for name in dic.keys():
    print(name+'\n')

# Value
for name in dic.values():
    print(name)

"""
4) set교집합
&, instersection()
"""
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)

"""
5) set합집합
|, union()
"""
print(a | b)

"""
6) set차집합
a-b
"""
print(a-b)

"""
7) set대칭차집합
a^b
"""
print(a ^ b)
