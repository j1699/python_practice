a = [1, 2, 3, 4]
b = a
a[0] = 4
print(a)
print(b)
print(a is b) # a, b 두개의 주소가 같은가?
# 즉 b = a로는 복사를 하는 것이 아니라 같은 주소를 공유함

b = a[:] # 슬라이싱을 통해 복사가 가능
a[0] = 1
print(a)
print(b)
# 이 기능을 from copy import coy
#           a = [1, 2, 3]
#           b = copy(a)를 통해서 복사 가능


# 변수 만들기
x = 1
a, b = ("python", "life") # (a, b) = ("python", "life"), [a, b] = ("python", "life")도 동일
print (a)
print(b)
c = d = "hello"
print(c)
print(d)
a = 3
b = 5
a, b = b, a # 변수값 바꾸기
print(a)
print(b)