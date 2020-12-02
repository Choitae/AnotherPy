def findinList(aList, target, key, start) :
    i = start
    length = len(aList)
    while i < length :
        if key + aList[i] == target :
            return i
        i += 1
    return -1 # -1을 리턴하므로써 main에서 if문을 사용하려는 것





aList = [4, 6, 9, 10, 2, 0,5]
target = int(input("값을 입력하세요"))
length = len(aList)
i = 0
while i < length -1:
    key = aList[i]
    pos = findinList(aList, target, key, i+1)
    if (pos > -1) :
           print(i, pos)

    else :
        print("값이 없습니다")
    i += 1



