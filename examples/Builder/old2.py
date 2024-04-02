class House:
    def __init__(self, walls, floor, door, windows, roof):
        self.walls = walls
        self.floor = floor
        self.door = door
        self.windows = windows
        self.roof = roof

# Subclasses representing different house configurations
class WoodenHouse(House):
    def __init__(self, door, windows):
        super().__init__(4, "wooden", door, windows, "shingle")

class BrickHouse(House):
    def __init__(self, door, windows):
        super().__init__(4, "brick", door, windows, "tile")

# Creating instances of different house configurations using subclasses
house1 = WoodenHouse("single", 2)
house2 = BrickHouse("double", 4)
