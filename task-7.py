course=str(input("Enter your course(Science/Commerce/Literature):")).capitalize()
match course:
   case "Science":
      value=str(input("Enter your sub-choice(Medical/Engineering):"))
      print("Science-",value)
   case "Commerce":
      value=str(input("Enter your sub-choice(CA/B.Com):"))
      print("Commerce",value)  
   case "Arts":
      value=str(input("Enter your sub-choice(History/Literature):"))
      print("Arts",value)
   case _:
      print("Not a Course") 