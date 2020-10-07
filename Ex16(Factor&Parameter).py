"""
함수의 인자값, 가변인자 다루
"""
def menu(w1,w2,w3):
    return {'red':w1,'green':w2,'yello':w3}

a=menu('빨강','녹색','노랑')
"""
print(a)
"""

def menu(ar,result=[]):
    result.append(ar)
    print(result)

#result변수가 공유된다.
"""
menu('a')
menu('b')
"""

#result변수가 공유되지 않는다.
"""
menu('a',[1,2])
menu('b',[3,4])
"""

def menu(ar,result=5):
    print(result)

"""
매개변수를 *를 사용하면 튜플
**를 사용하면 딕셔너리
"""
def menu(*text):
    result=''
    for s in text:
        result+=s
    return result

print(menu('a','b','c','d'))

def menu(**text):
    for i in text.keys():
        print('{0}={1}'.format(i,text[i]))

#menu(kor=90,eng=80,mat=70)

def menu(**text):
    tot=0
    for i in text.keys():
        print('{0}={1}'.format(i,text[i]))
        tot+=text[i]
    print(tot)

menu(kor=90,eng=80,mat=70)
