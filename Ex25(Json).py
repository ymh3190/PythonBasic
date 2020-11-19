"""
1) json 만들기 (딕셔너리 형태)
"""
"""
import json

info={'name':'유','age':30,'job':'programmer'}

k=json.dumps(info) # 사전형 데이터를 json형의 텍스트 문자열로 변경

#'./info.json','w' : .은 현재 디렉토리를 의미한다.
with open('C:/Users/Yoo/AppData/Local/Programs/Python/Python38-32/data/info.json','w') as f:
    json.dump(info,f) #info(dictionary)를 f(json)형태로 넣겠다
    #json.dump(info,f,ensure_ascii=False)

#ensure_ascili=False 한글로 저장
"""

"""
2) json 읽기
"""


with open('C:/Users/Yoo/AppData/Local/Programs/Python/Python38-32/data/info.json', 'r') as f:
    l_info = json.load(f)
print(l_info)
print(type(l_info))
