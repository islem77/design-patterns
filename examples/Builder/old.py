class House:
    def __init__(self, walls, floor, door, windows, roof):
        self.walls = walls
        self.floor = floor
        self.door = door
        self.windows = windows
        self.roof = roof

# Creating instances of different house configurations
woodenSinleHouse = House(4, "wooden", "single", 2, "shingle")
doubleBrickHouse = House(4, "brick", "double", 4, "tile")
