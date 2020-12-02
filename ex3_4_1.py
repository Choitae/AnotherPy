target = 9
aList = [4, 0, 5, 7, 9, 2, 4, 10, 18]
length = len(aList)
print("aList의 길이는", length)
bfind = False
i = 0

while i < length:
    j = i + 1
    while j< length :
           if(aList[i] + aList[j] == target):
               print(i, j)
               break

           j +=1
    i+=1


print("프로그램이 종료되었습니다")
