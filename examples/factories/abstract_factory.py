from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass

class Truck(Transport):
    def deliver(self):
        print("Delivering by truck...")

class Ship(Transport):
    def deliver(self):
        print("Delivering by ship...")

class TransportFactory(ABC):
    @abstractmethod
    def create_transport(self):
        pass

class TruckFactory(TransportFactory):
    def create_transport(self):
        return Truck()

class ShipFactory(TransportFactory):
    def create_transport(self):
        return Ship()

class LogisticsApp:
    def __init__(self):
        self.truck_factory = TruckFactory()
        self.ship_factory = ShipFactory()

    def deliver_package_by_truck(self):
        transport = self.truck_factory.create_transport()
        transport.deliver()

    def deliver_package_by_ship(self):
        transport = self.ship_factory.create_transport()
        transport.deliver()

if __name__ == "__main__":
    app = LogisticsApp()

    # Deliver package by truck
    app.deliver_package_by_truck()

    # Deliver package by ship
    app.deliver_package_by_ship()
