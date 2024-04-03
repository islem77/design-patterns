# Refactored code using the Composite pattern

class Component:
    def calculate_total_price(self):
        pass

class Product(Component):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate_total_price(self):
        return self.price

class Box(Component):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def calculate_total_price(self):
        total_price = 0
        for child in self.children:
            total_price += child.calculate_total_price()
        return total_price

# Usage
if __name__ == "__main__":
    # Creating products
    product1 = Product("Laptop", 1000)
    product2 = Product("Headphones", 100)
    
    # Creating boxes
    box1 = Box("Box 1")
    box1.add(product1)
    box1.add(product2)
    
    print("Total price of Box 1:", box1.calculate_total_price())
