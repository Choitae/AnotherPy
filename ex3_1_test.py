birth_m = int(input("태어난 달 : "))
today_m = int(input("현재 달 : "))
gap_m = today_m - birth_m

special_m_31 = 0
special_m_30 = 0
special_m_28 = 0

m = 0
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
print("31인 달은 : ", special_m_31)
print("30인 달은 : ", special_m_30)
print("28인 달은 : ", special_m_28)

