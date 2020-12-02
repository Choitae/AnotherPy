#가장 작은 커피(8oz)
small_size = 8
small_size_price = int(input("가장 작은 커피의 가격 : "))
small_size_1oz_price = small_size_price/small_size
print("작은 사이즈의 1oz당 가격은 : ", small_size_1oz_price)

#가장 큰 커피(20oz)
big_size = 20
big_size_price = int(input("가장 큰 커피의 가격 : "))
big_size_1oz_price = big_size_price / big_size
print("가장 큰 사이즈의 1oz당 가격은 : ", big_size_1oz_price)

#price = small_size_1oz_price <= big_size_1oz_price

#print("큰 사이즈 커피의 1oz당 가격이 더 비싸다는 것은", price, "이다")
#print(" 라지가 더 싼가? ", small_size_1oz_price >= big_size_1oz_price)

if small_size_1oz_price > big_size_1oz_price:
    print("큰  사이즈의 1oz 당 가격이 더 싸다")

elif small_size_1oz_price == big_size_1oz_price:
    print("두 커피의 가격은 모두 같다")

else :
    print("작은 사이즈의 ioz당 가격이 더 싸다")
