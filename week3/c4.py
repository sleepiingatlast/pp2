from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def show(self):
        print("координаты: ", self.x, self.y)
        
    def move(self, x, y):
        self.x = x
        self.y = y
        
    def dist(self, second):
        distance = sqrt(((self.x - second.x)**2) + ((self.y + second.y)**2))
        print(f"дитсанция между ({self.x}, {self.y}) и ({second.x}, {second.y}): {distance}")
        
coord1 = Point(1, 2)
coord1.show()
coord1.move(3, 4)
coord1.show()

coord2 = Point(5, 6)
coord2.dist(coord1)