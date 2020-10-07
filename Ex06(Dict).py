"""
1) 딕셔너리 만들기
{키:값,키:값,키:값...}의 형태
순서를 보장하지 않음
"""
dic={}
print(type(dic))
dic={'kor':80,'eng':90,'mat':77}
print(dic)

print(dic['eng']) #Key로 Value를 알 수 있다.

"""
2) 다른 객체를 딕셔너리로 변환
ex1) 리스트안의 리스트를 딕셔너리로 변환(튜플안의 튜플 형태도 동일)
ex2) 문자열을 딕셔너리로 변환(튜플 형태도 동일)
"""
#ex1
li=[['a','b'],['c','d'],['e','g']]
print(dict(li))
tup=(('ab'),('cd'),('ef'))
print(dict(tup))

#ex2
li=['ab','cd','ef']
print(dict(li))
tup=('ab','cd','ef')
print(dict(tup))

"""
3) 딕셔너리에 새로운 값 추가
ex) 딕셔너리는 값이 순차적으로 나오지 않는다.
"""
dic={'kor':80,'eng':90,'mat':77}
dic['tot']=247
print(dic)

"""
4) 딕셔너리 결합하기
"""
dic={'kor':80,'eng':90,'mat':77}
dic2={'kor2':88,'eng2':99,'mat2':77}
dic.update(dic2)
print(dic)

"""
5) 딕셔너리 항목 삭제하기
"""
dic={'kor':80,'eng':90,'mat':77}
del dic['mat']
print(dic)
#ex 모든 항목 삭제하기
dic.clear()
print(dic)

"""
6) 딕셔너리 항목 존재 유무 확인하기
"""
dic={'kor':80,'eng':90,'mat':77}
print('eng' in dic)

"""
7) 딕셔너리 항목 얻기
"""
dic={'kor':80,'eng':90,'mat':77}
print(dic.get('tot','not')) #존재하지 않는 키로 접근하면 not을 반환

"""
8) 모든 키 얻기
"""
dic={'kor':80,'eng':90,'mat':77}
print(dic.keys()) #필요시 리스트로 변환가능
print(list(dic.keys()))
print(dic.values())
print(dic.items())

"""
9) 모든 값 얻기
"""
print(list(dic.values()))

"""
10) 모든 순서쌍 얻기
"""
print(list(dic.items()))
m=list(dic.items())
print(m[1]) #리스트에 접근
print(m[1][1]) #리스트안의 튜플에 접근

"""
11) 딕셔너리 할당과 복사
"""
dic={'kor':80,'eng':90,'mat':77}
dic2=dic
print(dic)
print(dic2)
dic['tot']=247
print(dic)
print(dic2)

dic={'kor':80,'eng':90,'mat':77}
dic2=dic.copy()
dic['tot']=247
print(dic)
print(dic2)
