# python Exceptions (Errors)Handling


my_dict = {"a":1,"b":2,"c":3 }

try :
    value = my_dict["a"]
except IndexError:
    print("인덱스가 없어요~")
except KeyError:
    print("키가 없어요~")
except:
    print("뭔 문제가 발생했댜~ ")
else :
    print("에러가 없어요~ " )
