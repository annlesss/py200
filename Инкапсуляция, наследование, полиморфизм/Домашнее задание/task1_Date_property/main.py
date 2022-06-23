class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

        self.is_valid_date(self.day, self.month, self.year)

    # TODO какой декоратор следует применить?
    @staticmethod
    def is_leap_year(self, year: int) -> bool:
        """Проверяет, является ли год високосным"""

        # TODO записать условие проверки високосного года
        if self.year % 4 == 0:
            return True
        else:
            return False

    def get_max_day(self, month: int, year: int) -> int:
        """Возвращает максимальное количество дней в месяце для указанного года"""
        # TODO вернуть количество дней указанного месяца
        # посмотрела в пик солюшн, не поняла причем тут 0 и 1

    def is_valid_date(self, day: int, month: int, year: int) -> None:
        """Проверяет, является ли дата корректной"""
        # TODO если указанный набор день, месяц и год неверны, то вызвать ошибку ValueError
        if day > self.get_max_day(month, year):
            raise ValueError

    # TODO записать getter и setter для дня
    @property
    def day(self) -> int:
        return self._day

    @day.setter
    def day(self, day: int) -> None:
        if not isinstance(day, int):
            raise TypeError
        if not 1 <= day <= 31:
            raise ValueError
        self._day = day


    # TODO записать getter и setter для месяца
    @property
    def month(self) -> int:
        return self._month

    @month.setter
    def month(self, month: int) -> None:
        if not isinstance(month, int):
            raise TypeError
        if not 1 < month < 12:
            raise ValueError
        self._month = month


    # TODO записать getter и setter для года
    @property
    def year(self) -> int:
        return self._year
    @year.setter
    def year(self, year: int) -> None:
        if not isinstance(int):
            raise TypeError
        if not year > 0:
            raise ValueError
        self._year = year


if __name__ == "__main__":
    ...
