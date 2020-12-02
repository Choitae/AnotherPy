#시속 80km로 3시간 왕복 하는거리를 3시간 안에 다녀오야 된다. 가는 동안 60km 달렸다 , 제시간에 오려면 시속  몇 km로 달려야 하는가?

#총 거리
input("평균 왕복 속도 : "))*int(input("평균 왕복 시간 :"))

full_km = int(input("평균 왕복 속도 : "))*int(input("평균 왕복 시간 :"))
half_km = full_km/2

print("가는데 걸리는 시간 
#가는데 길막혔어~ 
go_speed = int(input("가는데 걸린 속도 : "))
go_hour = half_km/go_speed

back_hour = -go_hour
back_speed = half_km/back_hour

print("제 시간에 오려면 필요한 속도 : ", back_speed, "km/h")
