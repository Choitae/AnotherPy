#alist가 주어졋을 때 list 안에 최대값을 찾아 해당 index를 출력하시오

aList = [23,56, 12, 7, 9, 201, 33]
length = len(aList)
index = 0 # 현 위치
maxindex = 0 # 최고 숫자의 위치
bigNumber = 0

for x in aList:
    if bigNumber < x :
        bigNumber = x
        maxindex = index
    index += 1
    

print("위치 : ", maxindex)
# if max < alist[i]:
#     max = alist[i]
#    index = i
#  i += 1

