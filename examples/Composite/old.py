# Initial code without the Composite pattern

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Box:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_total_price(self):
        total_price = 0
        for product in self.products:
            total_price += product.price
        return total_price

# Usage
if __name__ == "__main__":
    # Creating products
    product1 = Product("Laptop", 1000)
    product2 = Product("Headphones", 100)
    
    # Creating boxes
    box1 = Box("Box 1")
    box1.add_product(product1)
    box1.add_product(product2)
    
    print("Total price of Box 1:", box1.calculate_total_price())
