kilometers = float(input("Enter a kilometers: "))
choice = input("Enter a converter type(meter/centimeter/millimeter/mile): ")
match choice:
    case "meter":
        result = kilometers * 1000
        print(kilometers,"kilometer is",result,"meter")
    case "centimeter":
        result = kilometers * 100000
        print(kilometers,"kilometer is",result,"centimeter")
    case "millimeter":
        result = kilometers * 1000000
     print(kilometers,"kilometer is",result,"millimeter")
    case "mile":
        result = kilometers * 0.621371
        print(kilometers,"kilometer is",result,"mile")
    case _:
        print("Invalid conversion")