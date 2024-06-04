"""
создайте класс `Plane`, наследник `Vehicle`
"""

from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload

class Plane(Vehicle):
    def __init__(self, cargo, max_cargo):
        self.cargo = cargo
        self.max_cargo = max_cargo

    def load_cargo(self, amount):
        if self.cargo + amount <= self.max_cargo:
            self.cargo += amount
        else:
            raise CargoOverload("Перегруз")

    def remove_all_cargo(self):
        current_cargo = self.cargo
        self.cargo = 0
        return current_cargo