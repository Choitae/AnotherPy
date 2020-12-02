# 1. 사람 찾아 번호 출력하기, 2. 새로운 사람 입력하기. 3. 종료하기.



numberNote = {} #딕셔너리 만들어두기 

while 1 :         # 왜 int로는 선언이 안되는가?
    select_num = float(input("1. 사람으로 번호찾기 / 2. 번호로 사람찾기 / 3. 등록하기 / 4. 번호 수정하기 / 그 외] 종료하기 : "))
    if  select_num == 1:
        name = input("이름 : ")
        for k in numberNote:
          if name == k : 
             print(name,"의 번호는 : ", numberNote[name])
          else :
             print("없습니다 ") # xxx
       # if (numberNote[name] == null) :  #이름이 없거나 번호가 없을 때
       #     print("없습니다 ")

        
                
    elif select_num == 2 :
         number = input("번호 : ")
         for k, v in numberNote.items() :
           if v == number :
              name = k
              print(number,"를 사용하는 사람은", name , "이다.")
           elif v != number :
              print("없습니다 ")

 

    elif select_num == 3 :
         numberNote[input("이름 : ")] = input("번호 : ")

    elif select_num == 4 :
         name = input("이름 : ")
         numberNote[name] = input("바꿀 번호 : ")
         print("이름 : ",name," 번호 : ", numberNote[name], "으로 변경되었습니다.")

    else :
        print("프로그램을 종료합니다")
        break

