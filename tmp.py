import json

info = {'name': '유', 'age': 30, 'job': 'programmer'}

k = json.dumps(info)  # 사전형 데이터를 json형의 텍스트 문자열로 변경

# './info.json','w' : .은 현재 디렉토리를 의미한다.
with open('./info.json', 'w') as f:
    json.dump(info, f)  # info(dictionary)를 f(json)형태로 넣겠다
    ensure_ascili = False
    # json.dump(info,f,ensure_ascii=False)

# ensure_ascili=False 한글로 저장
