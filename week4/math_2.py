import math

h = float(input("Enter the height of trapezoid: "))
base_1 = float(input("Enter the 1st value of base: "))
base_2 = float(input("Enter the 2nd value of base: "))

trapezoid_area = ((base_1 + base_2)/ 2) * (h)

print(f'Area: {trapezoid_area:.2f}')

# Height: 5
# Base, first value: 5
# Base, second value: 6
# Expected Output: 27.5