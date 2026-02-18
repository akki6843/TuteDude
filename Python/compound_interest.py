"""
Amount = P(1 + R/100) ** T
ci = Amount  - P
"""

P  = float(input("Enter the principal amount : "))
R = float(input("Enter the rate of interest : "))
T = float(input("Enter the time : "))

amount = P * (1 + R / 100) ** T

ci = amount - P

print(f"The area of the triangle with given price is {round(ci, 2)}")