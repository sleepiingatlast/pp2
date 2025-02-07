class Shape():
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self, length):
         self.length = length
    
    def area(self):
        return self.length * self.length
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
shape = Shape()
print(shape.area())

ex = float(input("введите сторону квадарата: "))
square = Square(ex)
print(square.area())

ex_length = float(input("введите длину прямоугольника: "))
ex_width = float(input("введите ширину прямоугольника: "))
rectangle = Rectangle(ex_length, ex_width)
print(rectangle.area())