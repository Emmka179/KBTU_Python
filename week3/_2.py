class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length * self.length

length = int(input("Enter the len: "))
sq = Square(length)
print("Square of area totally: ", sq.area())