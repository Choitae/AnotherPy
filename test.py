# python Exceptions (Errors)Handling
i = 0
b = []
while i<50:
    a = [1]*50 #파이썬에만 이렇게 된다.
    b.append(a)
    i+= 1
    a = 0


def oldOrange(a) :#a개
    for i in range (a):
        x = int(input("열 : "))
        y = int(input("행 : "))
        b[x][y] = 2

p = int(input("바꿀개수 : "))
oldOrange(p)
print(b)
