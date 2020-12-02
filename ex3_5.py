#주어진 배열 nums = [2,7,11,15]가 있을 때 배열 안의 두개의 원소를 더해
#주어진 target = 9에 만족할 때,
#해당 인덱스 [0,1]을 보여주는 프로그램을 작성하라


nums = [2,7,11,15]
length = len(nums)
target = 9
i = 0
result = []
resultposition = 0

while i < length-1:
    if (nums[i] + nums[i+1] == target):
        resultposition = i

    i +=1
        



print("합이 9가 되는 해당 인덱스는 ", nums[resultposition],"과 ",nums[resultposition+1],"이며",[resultposition, resultposition+1],"이다") 
