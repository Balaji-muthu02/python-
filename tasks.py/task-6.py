num=int(input("Enter a number:"))
match num:
   case num if num%3==0 and num%5==0:
      print("FizzBuzz")
   case num if num%5==0:
      print("Buzz")
   case num if num%3==0:
      print("Fizz")
   case _:
      print(num) 