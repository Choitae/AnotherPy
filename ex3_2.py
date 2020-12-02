#3개의 입력된 정수값에서 최대값을 구하는 프로그램을 작성하시오

num_f = int(input("첫 번째 값은 : "))
num_s = int(input("두 번째 값은 : "))
num_t = int(input("세 번째 값은 : "))

if num_f - num_s >= 0 and num_f - num_t > 0 :
    print("최대값은 ",num_f,"입니다")
elif num_f - num_s == 0 and num_f - num_t ==0:
    print("모든  정수 값은" ,num_f,"로 동일합니다")
elif num_f - num_s >= 0 and num_f - num_t < 0 :
    print("최대값은", num_t,"입니다")
elif num_f - num_s <0 and num_f - num_t> 0:
    print("최대값은", num_s, "입니다")
else :
     if num_s - num_t == 0:
         print("최대값은" , num_s, "입니다")
     elif num_s > num_t > 0:
         print("최대값은", num_s, "입니다")
     else :
         print("최대값은",num_t,"입니다")
