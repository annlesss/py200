# TODO Добавить методы add_water и remove_water
from typing import Union


class Glass:
    def __init__(self, capacity_volume, occupied_volume):
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume

    def add_water(self, capacity_volume, occupied_volume):


if __name__ == "__main__":
    glass = Glass(200, 100)  # экземпляр класса
    print(glass.capacity_volume, glass.occupied_volume)
