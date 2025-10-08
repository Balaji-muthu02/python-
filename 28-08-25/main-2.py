# c=int(input("enter the value"))
# d=int(input("enter the value"))

# rating=int(input("enter the rating"))
# match rating:
#     case 1:
       
# a=int(input("enter the temp"))
# if a>30:
#     print("hot")
# elif a>= 25 and a<=30:
#     print("warm")
# elif a>=15 and a<=24:
#     print("cool")
# elif a<15:
#     print("cold")

# s=int(input("enter score"))

# if s>=80:
#     print("excel")
# elif s>=50 and s<=79:
#     print("good")
# elif s>=30 and s<=49:
#     print("avg")
# elif s<=30:
#     print("poor")

# def dl_method(team_score, target_score, overs_left):
#     # Enter your code here
#     if team_score>=target_score:
#         print("Team wins by DL method")
#     elif team_score<target_score and overs_left == 0:
#         print("Team loses by DL method")
#     elif team_score<target_score and overs_left>0:
#         print("Match to be continued")


# a=int(input("enter the year"))
# if a%4==0 and a%400==0:
#     print("leaf")
# elif a%100

# m=int(input("enter mark"))
# match m:
#      case m if m>=80 and m<=100:
#         print("excellent")
#      case m>=60 and m<=79:
#         print("very good")
#      case m>=59 and m<=50:
#         print("good")
#      case m>=40 and m<=49:
#         print("avg")
#      case m>=0 and m<40:
#         print("fail")
#      case _:
#         print("not valid")

a=int(input("enter the value"))
b=int(input("enter the value"))

if a %3==0 and b%3==0:
   print("fizz")
else a %3==0 and b%5==0:
   print("buzz")
