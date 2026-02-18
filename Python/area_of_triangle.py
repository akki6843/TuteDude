"""
When all the length of the sides are known that is : a, b, c
Semi Perimeter - (s) = (a +b + c) / 2
Area = square root of (s * (s -a) * (s -b) * (s -c))
"""
a = float(input("Enter the first side  of the triangle:  "))
b = float(input("Enter the second side  of the triangle:  "))
c = float(input("Enter the third side  of the triangle:  "))

s = (a +b+c) / 2
area = (s * (s -a) * (s -b) * (s -c)) ** 0.5

print(f"The area of the triangle with given sides  is: {round(area, 2)}")