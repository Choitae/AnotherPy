#콘 아이스크림 2+1 행사와 3개의 가격과 같은 컵 아이스크림 30%할인 뭐가 이득인가?

#원래의 가격
con_icecream_value = 1000
cup_icecream_value = con_icecream_value*3
print("콘아이스크림 가격 : ", con_icecream_value, "  컵아이스크림 가격 : ", cup_icecream_value)

#이벤트 가격
con_icecream_value *= 2
cup_icecream_value *= 0.7
print("2+1의 콘아이스크림 가격 : ", con_icecream_value, "  할인된 컵아이스크림 가격 : ", cup_icecream_value)

#비교하기
if con_icecream_value > cup_icecream_value :
    print("콘 아이스크림을 구입하는 것이 이득이다")

elif con_icecream_value == cup_icecream_value :
    print("두 아이스크림의 구매 가격은 동일하다 ")

else :
    print("컵 아이스크림을 구매하는 것이 이득이다")
