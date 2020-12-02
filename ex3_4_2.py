def findlist(aList,     ):
    aList = [input("숫자를 입력하세요")]
    length = len(aList)
    number = 0;
    target = a
    while i < length:
        j = i + 1
        while j< length :
           if(aList[i] + aList[j] == target):
               print(i, j)
               number += 1
               break

           j +=1
        i+=1
    return number
findlist(9) 
