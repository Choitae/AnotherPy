#alist가 주어졋을 때 list 안에 최대값을 찾아 해당 index를 출력하시오

aList = [23,56, 12, 7, 9, 201, 33]
length = len(aList)
i = 0
bignumber = aList[0]
rule = i
while i < length-1:
    if bignumber - aList[i-1] > 0:
        bignumber = bignumber
        
    else :
        i += 1
        bignumber = aList[i]
        rule = i

    i += 1

print("위치 : ", rule)
# if max < alist[i]:
#     max = alist[i]
#    index = i
#  i += 1

