found_coin = int(input("내가 찾은 금화의 갯수"))
magic_coin = int(input("복제기계가 만든 금화의 갯수"))
stolen_coin = int(input("까마귀가 가져간 금화의 갯수"))
print(found_coin + magic_coin*365 - stolen_coin*52)
