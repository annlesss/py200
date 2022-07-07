from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """
    def __init__(self, value, next_):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value
        self.next = next_

    def __repr__(self):
        return f"Node({self.value}, None)" if self.next is None else f"Node({self.value}, {self.next})"

    def __str__(self):
        return str(self.value)

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    @property  # protected атрибут
    def next(self):
        return self._next

    @next.setter
    def next(self, next_: Optional):
        self.is_valid(next_)
        self._next = next_

    def __del__(self):
        print("Вызван метод \"__del__\"")




