"""
Simple interest = (P*R*T) / 100

P = principal;
R = rate of interest;
T = time
"""

P  = float(input("Enter the principal amount : "))
R = float(input("Enter the rate of interest : "))
T = float(input("Enter the time : "))

si = (P*R*T)/100
print(f"Simple interest :  {round(si, 2)}" )