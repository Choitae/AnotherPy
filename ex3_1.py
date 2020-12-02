#철수는 2000년 11월 3일에 태어났다
#오늘 2020년 11월 21은 태어난 지 며칠 째 되는 날인가?

#윤년은 4년에 1번씩 있다고 가정하자
#윤년은 연도를 4로 나누면 떨어지고 100으로 떨어지느 경우는 제외해야하며 연도가 400으로 나누어지면 포함시킨다.
# is_leap_year = ( year % 4 == 0 && year % 100 == 0 || year % 400 == 0)
# 한 해는 365일, 윤년은 366일 2020 / 2016 / 2012 / 2008 / 2004 / 2000

# 1, 3, 5, 7, 8, 10 , 12 --> 31일
# 2 --> 28일, 4, 6, 9, 11 --> 30일

birth_y = int(input("태어난 년도 : "))
birth_m = int(input("태어난 달 : "))
birth_d = int(input("태어난 일 : "))

print("태어난 연도는 {}년 {}월 {}일 입니다".format(birth_y,birth_m,birth_d))

today_y = int(input("현재 연도 : "))
today_m = int(input("현재 달 : "))
today_d = int(input("현재 일 : "))

print("현재 연도는 {}년 {}월 {}일 입니다".format(today_y,today_m,today_d))

gap_y = today_y - birth_y
gap_m = today_m - birth_m
gap_d = today_d - birth_d

y = birth_y
special_y = 0

m = 0
special_m_31 = 0
special_m_30 = 0
special_m_28 = 0


m = 0


if gap_y != 0:

    while y <=today_y:
        y +=1
        if y % 4 == 0:
            special_y +=1



    
    while m < today_m -1:
          m += 1 
          if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m==12:
             special_m_31 +=1
          elif m == 2:
             special_m_28 +=1
          else :
             special_m_30 +=1
 


    m = birth_m
    while birth_m -1 < m < 12:
          m += 1 
          if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m==12:
             special_m_31 +=1
          elif m == 2:
            special_m_28 +=1
          else :
            special_m_30 +=1

if (gap_y > 0) and (gap_m >= 0):
        gap_y == 0        
if gap_m != 0:
        m = birth_m
        if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m==12:
             birth_d = 31 - birth_d
        elif m == 2:
             birth_d = 28 - birth_d
        else :
             birth_d = 30 - birth_d
        gap_d = birth_d + today_d

    
print(special_y, gap_y, special_m_31, special_m_30, special_m_28, gap_d)
day = special_y*366 + (gap_y - special_y)*365 + special_m_31*31 + special_m_30*30 + special_m_28*28 + gap_d + 1
print("오늘은", day, "일 째 되는 날이다")


        
        
