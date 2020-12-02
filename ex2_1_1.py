#원래의 가격
con_icecream_value = int(input("콘  아이스크림 가격 : "))

cup_icecream_value = int(input(" 컵 아이스크림 가격 : "))

print("콘아이스크림 가격 : ", con_icecream_value, "  컵아이스크림 가격 : ", cup_icecream_value)

#이벤트 가격
event_plus = int(input("추가해주는 개수 : "))
rate = float(input("할인 퍼센트 : ")) /100
cup_icecream_value = cup_icecream_value*(1-rate)
con_icecream_value = event_plus*con_icecream_value

print("이벤트한 콘아이스크림 가격 : ", con_icecream_value, "  할인된 컵아이스크림 가격 : ", cup_icecream_value)

#size = cup_icecream_value <= con_icecream_value

#print("컵 아이스크림이 콘 아이스크림보다 싸다는 것은 " , size  , "이다")
#print( cup_icecream_value < con_icecream_value and "정답" or "거짓" ,"이다")
#비교하기
if con_icecream_value > cup_icecream_value :
    print("컵  아이스크림을 구입하는 것이 이득이다")

elif con_icecream_value == cup_icecream_value :
    print("두 아이스크림의 구매 가격은 동일하다 ")

else :
    print("콘 아이스크림을 구매하는 것이 이득이다")
