class Shape:
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

length = int(input("Enter the len: "))
width = int(input("Enter the width: "))
rect = Rectangle(length, width)
print("Square of rectangle totally: ", rect.area())