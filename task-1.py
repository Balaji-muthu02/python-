N=int(input("Enter a N value:"))
M=int(input("Enter a M value:"))
sum=M+N
match sum%2==0:
   case 1:
      print("Even")
   case _:
      print("Odd")  
