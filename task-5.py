a = int(input("1st side length:"))
b = int(input("2nd side length:"))
c = int(input("3rd side length:"))
if (a + b <= c) or (a + c <= b) or (b + c <= a):
    print("Not a valid triangle")
elif a == b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")