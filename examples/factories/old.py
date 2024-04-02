class LogisticsApp:
    def deliver_package(self, transport_type):
        if transport_type == 'truck':
            truck = Truck()
            truck.deliver()
        elif transport_type == 'ship':
            ship = Ship()
            ship.deliver()

class Truck:
    def deliver(self):
        print("Delivering by truck...")

class Ship:
    def deliver(self):
        print("Delivering by ship...")

if __name__ == "__main__":
    app = LogisticsApp()
    
    # Deliver package by truck
    app.deliver_package('truck')
    
    # Deliver package by ship
    app.deliver_package('ship')