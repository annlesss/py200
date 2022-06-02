from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        #  TODO инициализировать объект "Стакан"
        if not isinstance(capacity_volume,(int, float)):
            raise TypeError
        if not capacity_volume > 0:
            raise ValueError
        self.capacity_volume = capacity_volume  # объем стакана

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume < 0:
            raise ValueError
        self.occupied_volume = occupied_volume  # объем жижи в стакане



if __name__ == "__main__":
    glass1 = Glass(200, 120)  # TODO инициализировать два объекта типа Glass
    glass2 = Glass(500,50)
    print(glass1)
     # TODO попробовать инициализировать не корректные объекты
