current=str(input("Enter your type(residential/commercial):"))
match current:
   case "residential":
      unit=int(input("Enter your unit:"))
      sum1=100*3
      sum2=100*5
      sum3=sum1+sum2
      if unit<100:
        print(unit*3)
      elif 101>=unit or unit<=200:
        result=unit-100
        s=result*5
        print(sum1+s)  
      elif unit>=201:
        result=unit-200
        s=result*7
         print(sum3+s)
      else:
        print("invalid")  
   case "commercial":
      unit=int(input("Enter your unit:"))
      sum1=100*5
      sum2=100*7
      sum3=sum1+sum2
      if unit<100:
        print(unit*5)
      elif 101>=unit or num<=200:
        result=unit-100
        s=result*7
        print(sum1+s)  
      elif unit>=201:
        result=unit-200
        s=result*10
        print(sum3+s)
      else:
        print("invalid")  