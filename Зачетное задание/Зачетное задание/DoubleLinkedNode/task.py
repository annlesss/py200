from typing import Optional, Any
class Node:
    """ Класс, который описывает узел связного списка. """
    def __init__(self, value: Any, next_: Optional["Node"] = None):
        self.value = value
        self.next = next_

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"Node({self.value}, {None})" if self.value is None else f"Node({self.value}, {self._next})"

    def is_valid(self, node):
        if not isinstance(node, (type(None))):
            raise TypeError

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"]):
       # self.is_valid(next_)
        self._next = next_


class DoubleLinkedNode(Node):
    def __init__(self, value: Any, prev: Optional["Node"] = None, next_: Optional["Node"] = None):
        super().__init__(value, next_)
        self.prev = prev

    @property
    def _prev(self):
        return self.prev

    @_prev.setter
    def _prev(self, prev=None):
       # self.is_valid(prev)
        self.prev = prev

    def __repr__(self):
        return f"Node({self.value}, {None})" if self.value is None else f"Node({self.value}, {self.next}, {self.prev})"

    def __str__(self):
        super().__str__() # перегрузка метода
        return str(self.value)

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"]):
        #self.is_valid(next_)
        self._next = next_




if __name__ == "__main__":

    first_node = DoubleLinkedNode(1)
    second_node = DoubleLinkedNode(2)
    third_node = DoubleLinkedNode(3)

    first_node.next = second_node
    second_node.next = third_node
    third_node.next = None

    first_node._prev = None
    second_node._prev = first_node
    third_node._prev = second_node

    print(repr(first_node))
    print(repr(second_node))
    print(repr(third_node))
    print(repr(second_node.prev))
    print(repr(first_node.next))
    print(repr(first_node.prev))


