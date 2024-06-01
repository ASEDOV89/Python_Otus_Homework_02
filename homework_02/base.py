from abc import ABC


class Vehicle(ABC):
    def __init__(self, weight=1500, started=False, fuel=92, fuel_consumption=5):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
