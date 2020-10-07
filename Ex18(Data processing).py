"""
20강 파이썬 자료형을 활용한 데이터처리
"""

"""
이름    나이 국어 영어 수학
홍길동   22   77   88   90
김철수   32   87   67   30
이영희   29  100   70   84
김민우   11  100   90   89
문서영   13   95   97   92
"""

#딕셔너리
student = list()
student.append({'이름':'홍길동', '나이':22, '국어':77, '영어':88,'수학':90})
student.append({'이름':'김철수', '나이':32, '국어':87, '영어':67,'수학':30})
student.append({'이름':'이영희', '나이':29, '국어':100, '영어':70,'수학':84})
student.append({'이름':'김민우', '나이':11, '국어':100, '영어':90,'수학':89})
student.append({'이름':'문서영', '나이':13, '국어':95, '영어':97,'수학':92})

#1. 이영희의 총점과 평균을 구하세요.
total_score = student[2]['국어']+student[2]['영어']+student[2]['수학']
average_score = total_score / 3
print(total_score)
print(average_score)

#2. 이 반 학생의 나이의 합계를 구하세요.
age = 0
for i in range(len(student)):
    age += student[i]['나이']
print('이 반 학생의 나이 총합은', age)

#3. 이 반에서 모든 과목 중 가장 점수가 낮은 사람의 이름을 출력하세요.
min_student = {}
for i in student:
    if i['국어']<i['영어'] and i['국어']<i['수학']:
        min_student.update({i['이름']:i['국어']})
    elif i['영어']<i['국어'] and i['영어']<i['수학']:
        min_student.update({i['이름']:i['영어']})
    else:
        min_student.update({i['이름']:i['수학']})
    print(min_student)
li=sorted(min_student.items(), key=lambda x:x[1]) #딕셔너리 value값으로 정렬
print(li[0][0])
#print(sorted(min_student.items(), key=lambda x:x[1]))

#4. 반 평균보다 작은 사람의 이름을 구하세요.
average_score=0
average_class=0
for i in range(5):
    total_score=student[i]['국어']+student[i]['영어']+student[i]['수학']
    average_score+=total_score/3
average_class=average_score/5
print(average_class)

#5. 학급의 국어 총점은?
kor_score=0
for i in student:
    kor_score += i['국어']
print(kor_score)

#6. 성별이 '여'인 사람의 국어 총점은?
student = list()
student.append({'이름':'홍길동', '나이':22, '성별':'남', '국어':77, '영어':88,'수학':90})
student.append({'이름':'김철수', '나이':32, '성별':'남', '국어':87, '영어':67,'수학':30})
student.append({'이름':'이영희', '나이':29, '성별':'여', '국어':100, '영어':70,'수학':84})
student.append({'이름':'김민우', '나이':11, '성별':'남', '국어':100, '영어':90,'수학':89})
student.append({'이름':'문서영', '나이':13, '성별':'여', '국어':95, '영어':97,'수학':92})

kor_score=0
for i in student:
    if i['성별']=='여':
        kor_score+=i['국어']
print(kor_score)

#7. 성별이 '여'인 사람을 삭제하세요. 
for i in student:
    if i['성별']=='여':
        student.remove(i)
print(student)

#8. 총점을 추가하세요.
total_score=0
for i in student:
    total_score = i['국어']+i['영어']+i['수학']
    i['총점']=total_score

print(student)
print()

#9. 나이가 20대인 새로운 리스트를 만들어 보세요.
new_student=[]
for i in student:
    if i['나이'] >= 20 and i['나이'] < 30:
        new_student.append(i)

print(new_student)
    
