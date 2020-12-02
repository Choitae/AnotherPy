a = 1
b = 2
c = 2
d1 = a == b 
d2 = b != c
d3 = a > b
d4 = a >= b
d5 = b <=c
d6 = a < b
print("논리 연산자")
print(d1)
print(d2)
print(d3)
print(d4)
print(d5)
print(d6)

print("관계 연산자")
print(d1 and d2)
print(d2 and d4)
print(d1 and d6)
print(d1 or d5)
print(d1 or d2)
print(d5 or d6)
print(not d1)
print(not d5)

