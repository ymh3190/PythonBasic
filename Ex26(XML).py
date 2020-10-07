"""
1) XML 작성하기
<person>
    <name>홍길동</name>
    <age>22</age>
    <adress>대구</adress>
</person>
"""

from xml.etree.ElementTree import Element,dump,SubElement,ElementTree

#person=Element('Person')
person=Element('Person',time='14:03:00')

#Person에 추가하는 방법 1

name=Element('name')
name.text='홍길동'
person.append(name)
age=Element('age')
age.text='22'
person.append(age)

#Person에 추가하는 방법 2
SubElement(person,'address').text='대구'

#기존에 파일에 추가하기
no=Element('no')
no.text='17'
person.insert(1,no)

#삭제하기
person.remove(no)

#속성추가
#<Person date="2017-04-22">
person.attrib['date']='2017-04-22'

dump(person) #출력

"""
2) XML 파일로 저장하기
ElementTree(루트).write(경로)
"""
ElementTree(person).write('C:/Users/Yoo/AppData/Local/Programs/Python/Python38-32/data/person.xml')



















