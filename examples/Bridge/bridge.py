# Refactored code using the Bridge pattern

# Abstraction classes
class Shape:
    def __init__(self, color):
        self.color = color

    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        pass

class Square(Shape):
    def draw(self):
        pass

# Implementation classes
class Color:
    def fill(self):
        pass

class Red(Color):
    def fill(self):
        pass

class Blue(Color):
    def fill(self):
        pass

# Bridge classes
class CircleBridge(Circle):
    def __init__(self, color):
        super().__init__(color)

    def draw(self):
        self.color.fill()
        super().draw()

class SquareBridge(Square):
    def __init__(self, color):
        super().__init__(color)

    def draw(self):
        self.color.fill()
        super().draw()
