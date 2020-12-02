#앞으로 읽어도 뒤로 읽어도 같은 문자열이 되는 경우 인지 판단하는 프로그램을 작성
#Palindrome string ex) eye, madam --> true   // hellow --> false

A = str(input("단어를 입력하세요 :"))
B = len(A)
i = 0
while  i  < B :
    if A[i] == A[-1-i]: 
        i += 1
        if i == B-1:
            print("true")
       
    else:
        print("false")
        break

     
            

