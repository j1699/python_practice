s1 = set([1, 2, 3, 4, 5, 6]) # 집합은 중복 불가능
s2 = set([4, 5, 6, 7, 8, 9])
s1.add(10)
s2.update([11, 12, 13])
s1.remove(1)

print(s1 & s2) # 교집합
print(s1 | s2) # 합집합(a.union(b)로도 사용 가능)
print(s1 - s2) # 차집합(a.difference(b)로도 사용 가능)


a = [1, 2, 2, 3, 3, 4] # 집합을 활용하여 중복 제거
a = list(set(a))
print(a)