n=int(input("Enter a number:"))
m=n//10
j=n%10
sum1=m+j
sum2=m*j
result=sum1+sum2
match result==n:
   case 1:
      print("Great")
   case 0:
      print("Not great")  