class Shape():
    def area(self):
        return 0
class Square(Shape):
    def __init__(self,length):
        self.length=length
    def area(self):
        return self.length ** 2
    
a = float(input("a:"))
mysquare=Square(a)
print("area of the square:",mysquare.area())
myshape=Shape()
print("other:",myshape.area())
