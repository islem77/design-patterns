class Transport:
    def deliver(self):
        pass

class Truck(Transport):
    def deliver(self):
        print("Delivering by truck...")

class Ship(Transport):
    def deliver(self):
        print("Delivering by ship...")

class TransportFactory:
    def create_transport(self, transport_type):
        if transport_type == 'truck':
            return Truck()
        elif transport_type == 'ship':
            return Ship()

class LogisticsApp:
    def __init__(self):
        self.factory = TransportFactory()

    def deliver_package(self, transport_type):
        transport = self.factory.create_transport(transport_type)
        transport.deliver()

if __name__ == "__main__":
    app = LogisticsApp()

    # Deliver package by truck
    app.deliver_package('truck')

    # Deliver package by ship
    app.deliver_package('ship')
