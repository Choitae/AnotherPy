#스몰 사이즈 반지름 약 4인치 피자를 8등분하여 두조각을 담은 접시가 있다
#라지 사이즈 반지름  8인치 피자를 8등분 후 한조각을 담은 접시가 있다. 양 많은것은?

#스몰 사이즈 피자 크기

#import math : 수학이라는 메소드를 가져오는 것 (11월 21일)

import math

pi = math.pi
small_size_pizza_radius = int(input("스몰 사이즈 피자 반지름 : "))

print("스몰 사이즈 피자 반지름은 ", small_size_pizza_radius, "inch다")

amount_of_small_size_pizza = small_size_pizza_radius**2*pi

amount_of_divide_s = int(input("나누고 싶은 갯수 : "))
one_piece_of_small_size = amount_of_small_size_pizza/amount_of_divide_s
print("스몰 사이즈 한 조각의 양은 ", one_piece_of_small_size, "입니다.")

#라지 사이즈 피즈 크기
large_size_pizza_radius = int(input("라지 사이즈 피자 반지름 : "))

print("라지 사이즈 피자 반지름은 ", large_size_pizza_radius, "inch다")

amount_of_large_size_pizza = large_size_pizza_radius**2*pi

amount_of_divide_l = int(input("나누고 싶은 갯수 : "))

one_piece_of_large_size = amount_of_large_size_pizza / amount_of_divide_l
print("빅 사이즈 한 조각의 양은 ", one_piece_of_large_size, "입니다.")

#비교하기
print("피자의 양은 ", one_piece_of_large_size > one_piece_of_small_size and "라지가 많다" or "스몰이 많다")
print("피자의 양은 ", "라지가 적다" if one_piece_of_large_size < one_piece_of_small_size else "스몰이 적다")
