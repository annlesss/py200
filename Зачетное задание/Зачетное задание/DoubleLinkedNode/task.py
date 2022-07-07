from typing import Optional, Any
class Node:
    """ Класс, который описывает узел связного списка. """
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"Node({self.value}, {None})" if self.value is None else f"Node({self.value}, {self.next})"

    def is_valid(self, node):
        if not isinstance(node, (type(None), Node)):
            raise TypeError


class DoubleLinkedNode(Node):
    def __init__(self, value, next, prev):
        super().__init__(value, next)
        self.prev = prev

    @property
    def prev(self):
        return self.prev

    @prev.setter
    def prev(self):
        return self.prev

    def __repr__(self):
        return f"Node({self.value}, {None})" if self.value is None else f"Node({self.value}, {self.next})"

    def __str__(self):
        super().__str__() # перегрузка метода
        return str(self.value)


if __name__ == "__main__":
    ...
