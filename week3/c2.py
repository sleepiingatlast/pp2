class Shape():
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self, length):
         self.length = length
    
    def area(self):
        return self.length * self.length
    
shape = Shape()
print(shape.area())

ex = float(input("введите сторону квадрата: "))

square = Square(ex)
print(square.area())