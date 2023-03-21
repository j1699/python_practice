number = 10
day = "three"
a = "{name} ate %d apples. So {name} was {acting} for %s days." .format(acting="sick", name="MJ") %(number, day)
print(a)

b = "{} 만나서 반갑습니다".format("안녕하세요.")
print(b)

adress = "성북구"
c = f"저는 {adress}에 살고 있습니다."
print(c)