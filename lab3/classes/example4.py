import math #modul for sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point: ({self.x}, {self.y})")

    def move(self, x1, y1):
        self.x = x1
        self.y = y1

    def dist(self, point2):
        dx = self.x - point2.x
        dy = self.y - point2.y
        return math.sqrt(dx**2 + dy**2)


a = float(input("Enter x for point1: "))
b = float(input("Enter y for point1: "))
point1 = Point(a, b)


c = float(input("Enter x for point2: "))
d = float(input("Enter y for point2: "))
point2 = Point(c, d)


point1.show()
point2.show()


k = float(input("Enter new x for point1: "))
p = float(input("Enter new y for point1: "))
point1.move(k, p)
point1.show()

distance = point1.dist(point2)
print(f"Distance between point1 and point2: {distance}")
