#앞으로 읽어도 뒤로 읽어도 같은 문자열이 되는 경우 인지 판단하는 프로그램을 작성
#Palindrome string ex) eye, madam --> true   // hellow --> false

A = str(input("단어를 입력하세요 :"))
B = len(A)
i = 0
j = B - 1 
while  i  < j :
    if A[i] != A[j]: # + 문자열 시작부분부터 끝부분과의 비교를 실시.
        print("false")
        break
    else:
        i += 1
        j -= 1
else:
     print("true")
            

