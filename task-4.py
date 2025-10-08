num=int(input("Enter a KM:"))
match num:
   case num if num<=5:
      print(num*10)
   case num if 6>=num or num<14:
    sum1=5*10
    sum2=num-5
    sum3=sum2*8
    sum4=sum1+sum3
    print(sum4)
   case num if num==15:
    sum1=5*10
    sum2=10*8
    sum3=num-15
    sum4=sum1+sum2
    print(sum4)