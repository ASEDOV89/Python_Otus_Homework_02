from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel

class Vehicle(ABC):
    def __init__(self, weight=1500, started=False, fuel=150, fuel_consumption=5):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
                print("Автомобиль заведён")
            else:
                raise LowFuelError("Нет топлива, необходимо заправиться")

    def move(self, distance):
        if self.started:
            required_fuel = distance * self.fuel_consumption
            if required_fuel <= self.fuel:
                self.fuel -= required_fuel
                print(f"Мы преодолеем {distance} км с тем топливом, что есть в баке")
            else:
                raise NotEnoughFuel("Топлива не достаточно для преодоления указанной дистанции")
