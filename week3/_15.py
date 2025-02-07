import math

def sphere_vol(rad):
    return (4/3) * math.pi * rad**3

rad = float(input("Enter the radius: "))
print("The volume is:", sphere_vol(rad))