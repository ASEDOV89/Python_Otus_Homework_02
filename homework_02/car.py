"""
создайте класс `Car`, наследник `Vehicle`
"""

from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):
    def __init__(self, weight, started, fuel, fuel_consumption):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.engine = None

    def set_engine(self, engine: Engine):
        self.engine = engine
