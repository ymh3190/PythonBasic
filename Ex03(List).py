#리스트
"""
1) 문자열과 달리 변경 가능하다.
2) 대괄호[]로 구분한다.
ex) color = ['red', 'green', 'blue', 'yello']
"""
color = ['red', 'green', 'blue', 'yello']
print(color)
print(color[0])
color[0]='black'
print(color)

"""
3) 빈리스트 생성방법
3.1) 대괄호 사용
ex) em = []
3.2) 리스트함수 이용
ex) em2 = list()

"""
em=[]
print(em)
em2=list()
print(em2)

"""
4) 리스트 함수는 글자 하나하나 분리할 수 있다.
ex) m = list('good')
"""
m = list('good')
print(m)


"""
5) 튜플을 리스트로 변환하는 방법
ex) tup = ('a', 'b', 'c')
"""
tup = ('a', 'b', 'c')
print(tup)
print(type(tup))

m = list(tup)
print(m)
print(type(m))

"""
6) 문자열 나누기 -> split(리스트로 변환)
ex) day = '2016-05-12'
"""
day = '2016-05-12'
print(day)
k = day.split('-')
print(k)

"""
7) 인덱스로 리스트 접근하기
"""
li = ['a', 'b', 'c', 'd', 'e']
print(li[1])
print(li[0])
print(li[-1])
print(li[-2])

"""
8) 리스트의 항목 바꾸기
"""
li = ['a', 'b', 'c', 'd', 'e']
li[1] = 'bb'
print(li)

"""
9) 리스트 슬라이스 다루기
ex) [start:end-1]
ex) 오른쪽으로 2칸씩 : [::2]
ex) 역순으로 출력 : [::-1] 
"""
li = ['a', 'b', 'c', 'd', 'e']
print(li[0:2])
print(li[::2])
print(li[::-1])

"""
10) 리스트 항목 추가하기
ex) li.append('f')
"""
li = ['a', 'b', 'c', 'd', 'e']
li.append('f')
print(li)

"""
11) 리스트 병합하기
ex) li.extend(li2)
"""
li = ['a', 'b', 'c', 'd', 'e']
li2 = ['g', 'h']
li.extend(li2) # li += li2 도 가
print(li)
li3 = [1,2,3]
li += li3
print(li)

"""
12) 리스트 항목 삽입하기
ex) li.insert(인덱스,'aa')

"""
li = ['a', 'b', 'c', 'd', 'e', 'f']
li.insert(1,'aa')
print(li)


"""
13) 리스트 항목 삭제하기
ex) del li[인덱스]
"""
li = ['a', 'b', 'c', 'd', 'e', 'f']
del li[2]
print(li)

"""
14) 값으로 리스트 항목 삭제하기
ex) li.remove(값)
"""
li = ['a', 'b', 'c', 'd', 'e', 'f']
li.remove('e')
print(li)

"""
15) 항목을 얻은 후 삭제하기
ex) li.pop(인덱스)
"""
li = ['a', 'b', 'c', 'd', 'e', 'f']
a = li.pop(2)
print(a)

"""
16) 값으로 항목 위치 찾기
ex) li.index(값) -> 인덱스로 반환한다.
"""
li = ['a', 'b', 'c', 'd', 'e', 'f']
print(li.index('c'))

"""
17) 존재 여부 확인하기
ex) 값 in 리스트 -> true/false로 결과를 반환
"""
li = ['a', 'b', 'c', 'd', 'e', 'f']
print('b' in li)

"""
18) 특정 항목의 갯수 세기
ex) li.count(값)
"""
li = ['a', 'b', 'a', 'a', 'e', 'a']
print(li.count('a'))

"""
19) 리스트 문자열로 변환하기
ex) ','.join(리스트)
ex) '-'.join(리스트)
ex) ''.join(리스트)
"""
li = ['a', 'b', 'c', 'd', 'e', 'f']
print(','.join(li))
print('-'.join(li))
print(''.join(li))

#join과 split은 반대 개념이라 생각하면 된다.

"""
20) 정렬하기
sort()는 리스트 자체를 내부적으로 정렬한다.
li.sort(reverse=True)는 역순으로 정렬한다.
li.sorted()는 리스트의 정렬된 복사본을 반환한다.
"""
li = ['a', 'c', 'd', 'f', 'e', 'b']
li.sort()
print(li)
li.sort(reverse=True)
print(li)

a = sorted(li)
print(li)
print(a)

"""
21) 항목의 갯수 얻기
ex) len(리스트)
"""
li = ['a', 'b', 'c', 'd', 'e', 'f']
print(len(li))

"""
22) 리스트를 변수에 할당
ex) =
"""
li = ['a', 'b', 'c', 'd', 'e', 'f']
li2 = li #li과 li2는 같은 주소값을 사용한다.
li[0] = 'change'
print(li)
print(li2)

"""
23) 리스트를 새로운 리스트로 할당
ex) 리스트.copy()
ex) list(리스트)
ex) 리스트[:]
"""
a = ['a', 'b', 'c', 'd', 'e', 'f']
b = a.copy()
c = list(a)
d = a[:] # 콜론(:)이 의미하는 바는 a리스트의 처음부터 끝까지
a[0] = 'change'
print(a)
print(b)
print(c)
print(d)













