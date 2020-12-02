
import math

pi = math.pi

r_pizza_small = int(input("스몰사이즈 반지름: "))
piece_small = int(input("나누고 싶은 피자 개수 : "))
amount_small = r_pizza_small**2*pi/piece_small

r_pizza_large = int(input("라지사이즈 반지름: "))
piece_large = int(input("나누고 싶은 피자 개수 : "))
amount_large = r_pizza_large**2*pi/piece_large

if amount_large > amount_small:
    print("라지 사이즈가 더 양이 많습니다")
elif amount_large == amount_small:
    print("양은 같습니다")

else :
    print("스몰 사이즈가 더 양이 많습니다")

            

