#동일한 물건을 A매장에서는 20%, B매장에서는 10% 할인 후 11% 할인(중복할인)한다. 물건이 10,000원일 때 어던 쇼핑몰에서 싸게 살 수 있을까?

item_price = int(input("물품의 가격 : "))

#마켓 A에서의 할인율과 물품 가격
sale_percent_M_A = float(input("A 마켓 할인율 : ")) /100
market_a = item_price*(1-sale_percent_M_A)

print("A 매장에서의 할인된  물품 가격은", market_a, "원 이다")


#마켓 B에서의 할인율과 물품 가격
sale_percent_M_B_1 = float(input("B 마켓 1차 할인율 : ")) /100
sale_percent_M_B_2 = float(input("B 마켓 2차 할인율 : ")) /100
market_b = item_price*(1-sale_percent_M_B_1)*(1-sale_percent_M_B_2)

print("B 매장에서의 할인된 물품 가격은", market_b, "원 이다")
if market_b > market_a :
     print("마켓 A에서 물품을 구입하는 것이 더 낫다")
elif market_a == market_b:
     print("마켓 A와 마켓 B에서의 물품 가격은 동일하다")
else :
     print("마켓 B에서의 물품 가격이 더 싸다")
