# Existing code without the Bridge pattern

class Shape:
    def __init__(self):
        pass

class Circle(Shape):
    def draw(self):
        pass

class Square(Shape):
    def draw(self):
        pass

class RedCircle(Circle):
    def draw(self):
        pass

class RedSquare(Square):
    def draw(self):
        pass

class BlueCircle(Circle):
    def draw(self):
        pass

class BlueSquare(Square):
    def draw(self):
        pass
