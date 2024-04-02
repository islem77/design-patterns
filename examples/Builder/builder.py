class House:
    def __init__(self):
        self.walls = None
        self.floor = None
        self.door = None
        self.windows = None
        self.roof = None

    def __str__(self):
        return f"Walls: {self.walls}, Floor: {self.floor}, Door: {self.door}, Windows: {self.windows}, Roof: {self.roof}"

class HouseBuilder:
    def __init__(self):
        self.house = House()

    def set_walls(self, walls):
        self.house.walls = walls
        return self

    def set_floor(self, floor):
        self.house.floor = floor
        return self

    def set_door(self, door):
        self.house.door = door
        return self

    def set_windows(self, windows):
        self.house.windows = windows
        return self

    def set_roof(self, roof):
        self.house.roof = roof
        return self

    def build(self):
        return self.house

# Using the Builder pattern to construct different house configurations
builder = HouseBuilder()
house1 = builder.set_walls(4).set_floor("wooden").set_door("single").set_windows(2).set_roof("shingle").build()
house2 = builder.set_walls(4).set_floor("brick").set_door("double").set_windows(4).set_roof("tile").build()

print(house1)
print(house2)
