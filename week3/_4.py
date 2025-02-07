import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, x1, y2):
        self.x = x1
        self.y = y2

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)


x1 = int(input("Enter the x: "))
y1 = int(input("Enter the y: "))
x2 = int(input("Enter another point x: "))
y2 = int(input("Enter another point y: "))

point1 = Point(x1, y1)
point2 = Point(x2, y2)

point1.show()
point2.show()

print("Distance between points: ", point1.dist(point2))