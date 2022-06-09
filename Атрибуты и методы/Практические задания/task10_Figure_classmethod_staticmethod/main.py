import math


class TriangleCalculator:
    """ Класс-калькулятор площадей треугольников. """

    @classmethod  # нету никаких собственных атрибутов
    def area(cls, *args):   # метод экземпляра класса
        """
        Метод, который считает площадь по разным формулам,
         в зависимости от количества переданных аргументов.
        """
        if len(args) == 2:
            cls.area_by_height(*args)
        if len(args) == 3:
            cls.area_by_angle(*args)

    @staticmethod  # предназначены для операций, которые не воздействуют на класс или экземпляр класса
    def area_by_angle(a, b, angle):   # метод экземпляра класса
        """ Формула площади по двум сторонам и углу между ними. """
        return 0.5 * a * b * math.sin(angle)

    @staticmethod
    def area_by_height(a, h):  # метод экземпляра класса
        """ Формула площади по основанию и высоте. """
        return 0.5 * a * h


if __name__ == '__main__':
    TriangleCalculator().area()  # Работаем через экземпляр
    TriangleCalculator().area_by_height(5, 10)  # Работаем через экземпляр

    TriangleCalculator.area()  # Работаем через класс ( как с объектом )
    TriangleCalculator.area_by_height(5, 10)  # Работаем через класс ( как с объектом )

# тут без инита, так как