dic = {'name': 'Eric', "age": 15}
dic['phone num'] = '01057785967' # 추가
del dic['name'] # 삭제

print(dic)
print(dic["age"])
print(dic.keys())
print(dic.values())
print(dic.items())
print(dic.get('adress','없음'))
print('adress' in dic)


dic.clear()
print(dic) # dictionary 비우기