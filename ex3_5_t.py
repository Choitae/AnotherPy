alist = [2,7,11,15]
length = len(alist)
target = 9
print(len(alist))
def isEqual(target,a,b) :
    result = target==(a+b)
    return result
IsEqual = lambda target, a, b : target == (a+b) and True or False

for i in range(length-1) :
    for j in range(i+1,length -1) :
        if isEqual(target, alist[i], alist[j]):
            print(i, j)
        
